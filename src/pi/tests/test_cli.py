import json
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, "-m", "truck_gps", *args], cwd=ROOT,
                          capture_output=True, text=True, timeout=10)


class CliTests(unittest.TestCase):
    def test_default_demo_outputs_requests_not_hardware_feedback(self):
        result = run("--config", "config.example.toml", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual([row["fan_requested_pct"] for row in rows],
                         [0, 0, 30, 65, 100, 30, 0, 100, 0, 100, 100, 0])
        self.assertEqual(rows[7]["sensor_fault"], "missing_sensor")
        self.assertEqual(rows[9]["sensor_fault"], "stale_sensor")
        self.assertEqual([row["led_requested_pct"] for row in rows], [0, 0] + [5] * 9 + [0])
        self.assertTrue(all(row["simulated"] and row["fan_rpm"] is None for row in rows))
        self.assertTrue(all(row["gps_power"] is None for row in rows))
        self.assertIn("Simulation only", result.stderr)

    def test_bad_arguments_fail_without_output(self):
        for args in [("--mode", "hardware"), ("--interval", "0"), ("--interval", "nan"),
                     ("--loop",), ("--led-brightness", "101"), ("--config", "missing.toml")]:
            with self.subTest(args=args):
                result = run(*args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)

    def test_scenario_events_persist_and_override_initial_options(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.json"
            path.write_text(json.dumps([
                {"temperature_c": 25},
                {"temperature_c": 25, "fan_mode": "auto", "led_enabled": False},
                {"temperature_c": 25},
            ]))
            result = run("--scenario", str(path), "--format", "json", "--fan-mode", "boost",
                         "--led-on", "--led-brightness", "8")
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual([r["fan_requested_pct"] for r in rows], [100, 0, 0])
            self.assertEqual([r["led_requested_pct"] for r in rows], [8, 0, 0])
            self.assertTrue(all(r["led_brightness_setting_pct"] == 8 for r in rows))

    @unittest.skipIf(sys.platform == "win32", "POSIX signals and pipe polling")
    def test_sigterm_interrupts_realtime_wait(self):
        process = subprocess.Popen([sys.executable, "-m", "truck_gps", "--realtime", "--loop",
                                    "--interval", "60", "--format", "json"], cwd=ROOT,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            with selectors.DefaultSelector() as selector:
                selector.register(process.stdout, selectors.EVENT_READ)
                self.assertTrue(selector.select(timeout=5), "simulation did not start")
                first = json.loads(process.stdout.readline())
            self.assertTrue(first["simulated"])
            process.send_signal(signal.SIGTERM)
            _, stderr = process.communicate(timeout=5)
            self.assertEqual(process.returncode, 0, stderr)
            self.assertIn("Simulation stopped", stderr)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()
