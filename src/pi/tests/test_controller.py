import json
import math
import unittest

from truck_gps.config import Config
from truck_gps.controller import Controller
from truck_gps.display import render_json
from truck_gps.sensors import Reading, parse_w1


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(Config())

    def sample(self, temperature, now=0, **kwargs):
        return self.controller.step(Reading("gps-compartment", temperature, now), now, **kwargs)

    def test_hysteresis_and_ramp(self):
        temperatures = [25, 34, 35, 40, 45, 60, 34, 32, 34]
        expected = [0, 0, 30, 65, 100, 100, 30, 0, 0]
        actual = [self.sample(t, i).fan_requested_pct for i, t in enumerate(temperatures)]
        self.assertEqual(actual, expected)

    def test_sensor_faults_request_full_cooling_and_valid_json(self):
        cases = [
            (None, "missing_sensor"),
            (Reading("other", 25, 100), "wrong_sensor"),
            (Reading("gps-compartment", 25, 84), "stale_sensor"),
            (Reading("gps-compartment", 25, 101), "future_timestamp"),
            (Reading("gps-compartment", 25, math.nan), "invalid_timestamp"),
            (Reading("gps-compartment", None, 100, "crc_error"), "crc_error"),
            (Reading("gps-compartment", math.nan, 100), "invalid_temperature"),
            (Reading("gps-compartment", math.inf, 100), "invalid_temperature"),
            (Reading("gps-compartment", True, 100), "invalid_temperature"),
            (Reading("gps-compartment", 101, 100), "temperature_out_of_range"),
            (Reading("gps-compartment", -41, 100), "temperature_out_of_range"),
        ]
        for reading, fault in cases:
            with self.subTest(fault=fault, reading=reading):
                status = self.controller.step(reading, 100)
                self.assertEqual(status.fan_requested_pct, 100)
                self.assertEqual(status.sensor_fault, fault)
                self.assertIsNone(json.loads(render_json(status))["temperature_c"])

    def test_reading_at_stale_boundary_is_valid(self):
        status = self.controller.step(Reading("gps-compartment", 25, 85), 100)
        self.assertIsNone(status.sensor_fault)
        self.assertEqual(status.sensor_age_s, 15)

    def test_boost_does_not_hide_sensor_fault(self):
        status = self.controller.step(None, 0, fan_mode="boost")
        self.assertEqual(status.fan_reason, "sensor_fault")
        self.assertEqual(status.sensor_fault, "missing_sensor")

    def test_fault_recovery_keeps_hysteresis_until_stop(self):
        self.controller.step(None, 0)
        self.assertEqual(self.sample(33, 1).fan_requested_pct, 30)
        self.assertEqual(self.sample(32, 2).fan_requested_pct, 0)

    def test_boost_release_keeps_hysteresis_until_stop(self):
        self.assertEqual(self.sample(25, 0, fan_mode="boost").fan_requested_pct, 100)
        self.assertEqual(self.sample(33, 1).fan_requested_pct, 30)
        self.assertEqual(self.sample(32, 2).fan_requested_pct, 0)

    def test_led_switch_preserves_setting_and_does_not_change_fan(self):
        on = self.sample(40, led_enabled=True, led_brightness_pct=7)
        off = self.sample(40, led_enabled=False, led_brightness_pct=7)
        self.assertEqual(on.led_requested_pct, 7)
        self.assertEqual(off.led_requested_pct, 0)
        self.assertEqual(off.led_brightness_setting_pct, 7)
        self.assertEqual(on.fan_requested_pct, off.fan_requested_pct)

    def test_restart_does_not_reuse_old_state(self):
        self.sample(40)
        restarted = Controller(Config())
        status = restarted.step(Reading("gps-compartment", 33, 0), 0)
        self.assertEqual(status.fan_requested_pct, 0)
        self.assertFalse(status.led_enabled)
        self.assertEqual(restarted.step(None, 1).fan_requested_pct, 100)

    def test_feedback_is_unknown_in_simulation(self):
        status = self.sample(40)
        self.assertTrue(status.simulated)
        self.assertIsNone(status.fan_rpm)
        self.assertIsNone(status.gps_power)

    def test_invalid_commands_rejected(self):
        for options in [dict(fan_mode="off"), dict(led_enabled=1), dict(led_brightness_pct=101)]:
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.sample(30, **options)
        self.sample(30, 10)
        with self.assertRaises(ValueError):
            self.sample(30, 9)


class ParserTests(unittest.TestCase):
    def test_signed_and_zero_temperatures(self):
        for value in [0, -12500, 25125]:
            with self.subTest(value=value):
                reading = parse_w1(f"aa bb : crc=ff YES\naa bb t={value}\n", "sensor", 12)
                self.assertEqual(reading.temperature_c, value / 1000)
                self.assertEqual(reading.sampled_at_s, 12)
                self.assertIsNone(reading.error)

    def test_invalid_samples_never_become_zero(self):
        cases = [
            ("", "missing_sample"),
            ("x" * 4097, "oversized_sample"),
            ("one line", "malformed_sample"),
            ("aa NO\naa t=20000", "crc_error"),
            ("aa YES\naa missing", "malformed_temperature"),
            ("aa YES\naa t=20junk", "malformed_temperature"),
        ]
        for text, fault in cases:
            with self.subTest(fault=fault):
                reading = parse_w1(text, "sensor", 0)
                self.assertIsNone(reading.temperature_c)
                self.assertEqual(reading.error, fault)
