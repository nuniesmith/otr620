# Truck GPS controller: simulation milestone

Runnable control logic for the planned **Raspberry Pi Zero 2 W / Raspberry Pi OS Lite** installation. Requires Python **3.11 or newer** and has no runtime dependencies outside the standard library. GPIO, physical sensors, fan PWM, buttons, OLED, GPS power switching and telemetry are **not implemented**. The only supported mode is `simulate`.

## Run now, without Pi hardware

From the repository root:

```sh
cd src/pi
python3 -m truck_gps --config config.example.toml
python3 -m truck_gps --config config.example.toml --format json
python3 -m unittest discover -s tests -v
```

The built-in 12-sample demo completes immediately. Each sample advances a virtual clock by five seconds. Use `--realtime` to pace samples in wall-clock time, or `--realtime --loop` for a continuous demonstration. The timestamps still represent **scenario time**, not measured sensor acquisition time. Ctrl+C or SIGTERM interrupts the wait and exits cleanly.

For an installed command, use a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/truck-gps --format json
```

Building the package requires setuptools; pip may download the build tooling. No Raspberry Pi or GPIO packages are needed for simulation. Keep local settings in `config.local.toml` (ignored by git); do not put credentials in configuration files committed to the repository.

## Control behavior

These values are **bench starting settings**, not validated GPS/charger protection limits. Adjust only after choosing sensor placement and measuring the actual installation.

| Condition | Requested fan duty with the example configuration |
|---|---|
| Fresh startup, valid temperature below 35°C | 0% |
| Temperature reaches 35°C | 30% |
| Temperature rises from 35°C to 45°C | Linear increase from 30% to 100% |
| Temperature at or above 45°C | 100% |
| Active fan cools below 35°C but remains above 32°C | Hold 30% |
| Temperature reaches 32°C or lower | 0% |
| Manual `boost` | 100% |
| Missing, invalid, wrong-ID or stale sensor reading | 100% and an explicit fault |

A reading becomes stale when its age **exceeds** 15 seconds. A future or invalid timestamp is a fault. Sensor faults take priority over manual mode. There is deliberately no manual force-off mode. After a fault or boost, automatic control keeps the fan active until the stop threshold is reached. Restarting the process resets the hysteresis latch and command state; it does not preserve settings from earlier runs.

The 30% minimum is a requested value, not a verified starting or sustainable fan speed. Startup kick, calibrated minimum duty, electrical fallback and measured RPM remain hardware work. A software request for full cooling cannot guarantee cooling if the fan supply or controller fails.

LEDs default off with a stored brightness of 5%. Turning them off preserves the setting. LED commands do not affect fan decisions. `--led-on`, `--led-brightness 8` and `--fan-mode boost` set **initial** commands; later scenario events can change them. Brightness alone does not enable the LEDs. In particular, the built-in demo intentionally changes LED and fan modes.

## Custom scenarios

```sh
python3 -m truck_gps --scenario scenarios/example.json --format json
```

A scenario is a JSON array. Each row must contain exactly one sample source:

- `"temperature_c": 40` for a valid numeric reading, or `null` for a missing sensor.
- `"error": "disconnected"` for a reported sensor fault.
- `"w1_text": "aa YES\naa t=35000"` to exercise parsing of a captured Linux 1-Wire text sample.

Optional fields are `age_s` (default 0), `fan_mode` (`auto` or `boost`), `led_enabled` (boolean) and `led_brightness_pct` (0–100). Command changes persist into following rows until changed again. A repeated scenario retains command and hysteresis state across the loop boundary. Temperature/source and age apply to their own row only. Unknown keys, non-finite numbers, invalid commands and malformed configuration are rejected before the simulation starts. Out-of-range finite temperatures are accepted as scenario inputs and become controller faults.

The 1-Wire parser checks the kernel's `YES` CRC result marker and temperature format. It does not independently calculate CRC or read `/sys`. There are no device reads or retry loops yet; bounded acquisition and freshness tracking must be implemented for live sensors.

## Output and verification

Text output labels all values as requests. `--format json` emits one status object per line to stdout, with logs on stderr. `simulated` is always `true`; `fan_rpm` and `gps_power` are always `null` (unknown). No RPM, GPS state or power feedback is invented. `sensor_id` identifies the configured expected sensor, not necessarily a connected device.

All 21 tests passed on Linux with Python 3.12.14. Wheel building, installation into a clean virtual environment and the installed CLI demo also passed. Tests cover the fan curve and hysteresis, fault priority/recovery, stale boundaries, malformed readings, configuration validation, LED independence, restart state, CLI output and SIGTERM handling. They verify software decisions only. No physical fan, sensor, OLED, GPIO timing or Raspberry Pi installation has been tested.

## Optional Linux service example

[`systemd/truck-gps-sim.service`](systemd/truck-gps-sim.service) is a **simulation-only template**, not a production cooling service. It loops the demo and logs JSON to the journal. To use it later, install the package in `/opt/truck-gps/.venv`, copy settings to `/etc/truck-gps/config.toml`, create a dedicated `truck-gps` service account with read access to those paths, and install the unit in `/etc/systemd/system/`. Then reload systemd and start `truck-gps-sim.service`; enable boot startup only if wanted. Use `journalctl -u truck-gps-sim.service` to inspect output.

The template deliberately denies device access. Do not adapt it for live hardware merely by removing that restriction: implement and test the GPIO/sensor adapters and their permissions first. Neither this unit nor a restart policy provides an electrical cooling fallback or a Linux power-hold/shutdown circuit.

## Next implementation work

1. Record the installed Pi OS/Python versions and verify hardware PWM support for that board/OS.
2. Select the fan interface and validate the protected 5 V branch, PWM waveform and boot/crash state on the bench.
3. Add identified live temperature sensors with bounded acquisition and stale-data handling independent of control ticks.
4. Add fan/LED adapters, debounced buttons and optional tach feedback, then an OLED using shared state.
5. Validate systemd permissions, restart and power-hold/shutdown behavior before installation in the truck.
6. Add independent GNSS logging, Tailscale and the home map later.

See [the hardware and first-boot plan](../../docs/pi-setup.md) and [the project tasks](../../docs/todo.md). The Garmin initially stays on its supplied power arrangement. v0.4 CAD awaits fit results and actual component measurements.
