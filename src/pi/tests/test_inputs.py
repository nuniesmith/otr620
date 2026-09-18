import json
from pathlib import Path
import tempfile
import unittest

from truck_gps.config import Config, load_config, number
from truck_gps.simulation import load_scenario, reading_from_row


class InputTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "input"

    def test_example_config_loads(self):
        path = Path(__file__).resolve().parents[1] / "config.example.toml"
        self.assertEqual(load_config(path), Config())

    def test_invalid_config_is_rejected(self):
        cases = [
            "[fans]\nstart_c=35", "[fan]\nstrat_c=35", "fan=35",
            "[fan]\nstop_c=40", "[fan]\nfull_c=35", "[fan]\nmin_duty_pct=0",
            "[fan]\nstart_c=nan", "[fan]\nstart_c=true", "[fan]\nmin_duty_pct=101",
            "[sensor]\nstale_after_s=0", "[sensor]\nid=''", "[sensor]\nmax_valid_c=40",
            "[led]\nenabled=1", "[led]\nbrightness_pct=-1", "not valid toml",
        ]
        for content in cases:
            with self.subTest(content=content):
                self.path.write_text(content)
                with self.assertRaises(ValueError):
                    load_config(self.path)

    def test_extreme_numbers_are_rejected_cleanly(self):
        with self.assertRaises(ValueError):
            number(10 ** 1000, "huge")

    def test_invalid_scenarios_are_rejected(self):
        cases = [
            [], {}, [None], [{}], [{"temperature_c": 30, "typo": 1}],
            [{"temperature_c": 30, "error": "crc_error"}], [{"temperature_c": True}],
            [{"temperature_c": float("nan")}], [{"temperature_c": 30, "age_s": -1}],
            [{"temperature_c": 30, "fan_mode": "off"}], [{"temperature_c": 30, "led_enabled": 1}],
            [{"temperature_c": 30, "led_brightness_pct": 101}], [{"error": ""}], [{"w1_text": 25}],
        ]
        for rows in cases:
            with self.subTest(rows=rows):
                self.path.write_text(json.dumps(rows))
                with self.assertRaises(ValueError):
                    load_scenario(self.path)

    def test_scenario_sources(self):
        rows = [{"temperature_c": None}, {"error": "disconnected"},
                {"w1_text": "aa YES\naa t=35000", "age_s": 3}]
        self.path.write_text(json.dumps(rows))
        parsed = load_scenario(self.path)
        self.assertIsNone(reading_from_row(parsed[0], "sensor", 10))
        self.assertEqual(reading_from_row(parsed[1], "sensor", 10).error, "disconnected")
        reading = reading_from_row(parsed[2], "sensor", 10)
        self.assertEqual((reading.temperature_c, reading.sampled_at_s), (35, 7))
