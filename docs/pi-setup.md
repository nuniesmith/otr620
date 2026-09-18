# Pi setup and implementation plan

[Project](../README.md) · [Tasks](todo.md) · [V3.1 print notes](../src/stl/v0.3/README.md)

Status: **simulation software implemented; hardware integration pending**. The earlier review of commit `f8075d72dddf59a85583dda3cea287938e356ffc` found no `src/pi/` directory and withdrew incomplete README snippets. The first package now implements deterministic fan/LED decisions, fault handling, configuration, console status and tests. It has no physical outputs or live sensor reads. No v0.4 CAD has been generated. See [running instructions](../src/pi/README.md).

## Decisions and outstanding choices

- Selected fan: **Noctua NF-A4x20 5V PWM**, four-pin, with temperature-based speed control and a manual override.
- Selected host: **Raspberry Pi Zero 2 W with Raspberry Pi OS Lite**, confirmed by the user for full Linux services and low-level peripheral control. A Pico is not required for the initial design.
- Keep the Garmin on its supplied power arrangement for initial tests. The Pi supervises accessories; a rated power-distribution circuit supplies their current.
- The Pi Zero 2 W is selected. Choose the exact OLED module, switches, regulator and GNSS receiver before freezing pin assignments and enclosure cutouts.
- The user is printing the four v0.2 test pieces. Printing has started; no physical fit result is recorded yet.

The Zero 2 W uses micro-USB connectors and 2.4 GHz Wi-Fi. A USB-C panel inlet would therefore be part of the mount's power design, not the Pi's native connector. Confirm the truck network supports the board and include adapter/cable space in CAD. [Raspberry Pi specifications](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)

## Selected fan and proposed interface

| Item | Manufacturer specification |
|---|---|
| Model | NF-A4x20 5V PWM |
| Body / with pads | 40 × 40 × 20 mm / 40 × 40 × 22 mm |
| Mounting-hole spacing | 32 × 32 mm |
| Supply / maximum current | 5 V / 0.1 A |
| Connector | Four-pin |
| Speed at 0% PWM | Stopped |

Source: [Noctua model specifications](https://www.noctua.at/en/products/nf-a4x20-5v-pwm/specifications). Confirm dimensions on the actual part. A 22 mm body envelope is not sufficient evidence for a 22 mm printed pocket: add fit tolerance, connector access, wire bends, mounts and unobstructed intake/exhaust space. The current lower cavity is about 29.8 mm deep and the sound opening about 39.4 mm high; installation needs a geometry review.

| Fan pin | Manufacturer wire colour | Proposed connection |
|---|---|---|
| 1 | Black | Common ground |
| 2 | Yellow | Protected, regulated 5 V fan branch |
| 3 | Green | Optional tachometer input with a suitable 3.3 V pull-up/interface |
| 4 | Blue | Dedicated PWM control interface; never join to the ground conductor |

Verify connector orientation and pin numbers, especially with adapters. The manufacturer's colours supersede the older README's red supply-wire label. Fan power must not come from a GPIO output.

Use a **25 kHz target** with the manufacturer's allowed **21–28 kHz** range. Noctua describes an internal PWM pull-up, recommends a CMOS-style driver and does not recommend an open-collector driver for its fans. Select a Pi-compatible interface after checking the actual fan's pull-up voltage and powered/unpowered conditions; direct GPIO compatibility is not established by the old drawing. With no PWM input, the fan runs at full speed, but a crashed output held low may instead leave it stopped. Design and test fault handling accordingly. [Noctua PWM white paper](https://noctua.at/pub/media/wysiwyg/Noctua_PWM_specifications_white_paper.pdf)

GPIO18 is a candidate signal pin, not a finalized wiring instruction. `RPi.GPIO.PWM()` produces software PWM; using GPIO18 does not automatically select hardware PWM. Choose and verify a hardware PWM backend for the selected board/OS, or use a dedicated controller. [RPi.GPIO project documentation](https://pypi.org/project/RPi.GPIO/)

## Review findings to resolve in implementation

| Finding in the previous examples | Required behavior |
|---|---|
| Missing sensor returns an empty string and the caller indexes it | Return a typed fault; survive missing files, disconnects and malformed data. |
| CRC retry loop has no deadline | Bound retries and stale-reading age; controller ticks must keep running. |
| Missing temperature marker becomes 0°C | Do not interpret errors as a cold compartment. Enter a documented fallback state. |
| First discovered sensor is used without identity | Configure sensor IDs and distinguish GPS compartment, charger and Pi CPU readings. |
| Software PWM is labelled hardware PWM | Verify waveform frequency and duty under CPU/network load. |
| OLED uses fixed fan/GPS/LED values | Read shared controller state; distinguish requested duty, measured RPM and unavailable feedback. |
| Network subprocesses have no timeout | Bound calls and keep display/network failures independent of thermal control. |
| Abrupt master power-off is assumed | Define shutdown request, power-hold hardware and restart behavior before connecting ignition control. |
| GPS data source is unspecified | Verify a usable live Garmin interface or select a supported external GNSS receiver. |

On temperature-sensor failure, the simulation requests full cooling and reports a fault; a future hardware adapter must apply that request while the fan branch is powered. This software policy cannot guarantee cooling during a power failure or a crashed GPIO driver; bench-test the electrical default state. The implemented simulation permits auto or full-speed boost; sensor faults take priority. A force-off mode is not provided. Validate the policy with the physical hardware before use.

The earlier 35–45°C ramp is a **bench starting proposal**, not a validated protection limit. Simulation uses 35°C start, 32°C stop and a provisional 30% minimum request. Startup behavior and minimum stable duty still need physical calibration. Calibrate against actual sensor placement and the GPS/charger operating limits. A housing sensor does not measure the device's internal battery temperature.

## Software status under src/pi

Run the package with Python 3.11+; no GPIO libraries are imported. The only supported mode is `simulate`.

```sh
cd src/pi
python3 -m truck_gps --config config.example.toml --format json
python3 -m unittest discover -s tests -v
```

| File | Implemented now | Remaining hardware work |
|---|---|---|
| `README.md`, `pyproject.toml` | Quickstart and installable CLI, no external runtime dependencies | Verify on the actual Pi OS/Python |
| `config.example.toml`, `truck_gps/config.py` | Validated thresholds, expected sensor ID and LED settings | Pin/interface configuration after hardware selection |
| `truck_gps/sensors.py` | Pure captured 1-Wire sample parser and typed faults | Identified device reads with bounded acquisition |
| `truck_gps/hardware.py` | Simulation output adapter only | Verified PWM/GPIO adapters, boot/crash behavior |
| `truck_gps/controller.py` | Fan curve/hysteresis, auto/boost, LED requests and fault priority | Startup kick/minimum-duty calibration and buttons |
| `truck_gps/display.py` | Text/JSON status; RPM and GPS power explicitly unknown | OLED renderer, bounded network status |
| `truck_gps/main.py`, `truck_gps/simulation.py` | Validated scenarios, virtual time, logging and signal handling | Live acquisition/control scheduling |
| `systemd/truck-gps-sim.service` | Optional simulation-only template denying device access | Actual Pi installation and production service permissions |
| `tests/` | 21 passing software tests, including CLI/SIGTERM | Physical sensor/fan/output and Pi boot tests |

The demo runs immediately by default; `--realtime --loop` paces a repeating scenario. It does not run a real temperature acquisition loop. Scenario timestamps are virtual. A hardware service must use actual monotonic sample times and keep reads, display/network operations and control scheduling independent.

Keep the control loop local and independent of Tailscale, maps, OLED and internet availability. Use a Python virtual environment and a service account with only the needed device permissions. Keep credentials outside the repository. Read [the package documentation](../src/pi/README.md) for configuration, fault recovery and service-template limitations.

## Bring-up sequence when the Pi arrives

1. Use Raspberry Pi Imager to install an OS Lite image supported by the selected board. Configure hostname, user, Wi-Fi country/network and SSH access. Boot on a suitable bench supply. [Official setup guide](https://www.raspberrypi.com/documentation/computers/getting-started.html)
2. Update the OS, record its version and establish SSH. Install Tailscale using its current Linux instructions and verify access from an authorized device. [Tailscale installation](https://tailscale.com/docs/install/linux)
3. Enable I²C and 1-Wire using the selected OS configuration tools. Test the identified temperature sensor and exact OLED module separately. Match SSD1306 versus SH1106 drivers and verify supply and pull-up voltages. [Pi configuration guide](https://www.raspberrypi.com/documentation/computers/configuration.html)
4. Run the existing package and simulation tests on the Pi; record the OS/Python versions. Freeze board/OS-specific GPIO dependencies only after verifying support.
5. Implement live sensor acquisition and the hardware adapter. With the selected PWM interface and protected fan supply, test commanded duty, startup, stopping, optional tach feedback and sensor disconnection. Verify timing under load.
6. Add dim LEDs and debounced buttons. Verify that accessory switching does not interrupt the Garmin branch.
7. Add the service and test reboot, service crash, missing OLED, Wi-Fi loss and controlled shutdown. Do not rely on service restarts alone as the fan's electrical fallback.
8. Add GNSS logging and the home map later. Validate no-fix/stale-fix handling, trip distance, year boundaries and storage retention before adding traffic APIs. Keep trip data usable during network outages.

## v0.4 preparation after fit tests

Use `src/stl/v0.4/` for the next mechanical revision once inputs are available; it does not exist yet. Preserve the older session files.

- Record v0.2 face-frame, depth-gauge, bolt-trap and shelf-pocket results. The round v0.2 PopGrip seat does not validate the oval accessory.
- Test the v0.3 faceplate tabs and M2 nut pockets separately.
- Confirm the cubby measurement starts at the top of the black floor lip; measure taper, corners and shelf/control clearance.
- Measure the chosen electronics, switches, fan, connectors and cable bends. Keep GPS-dependent geometry provisional until the unit arrives.
- Design a removable electronics carrier, adjustable fan mount, separate ventilation path, serviceable wiring and modular display/switch cutouts.
- Maintain the padded GPS support, removable faceplate, speaker path and upward-facing accessory tray.
- Print new local fit coupons before exporting the complete v0.4 assembly. Check bed footprint, supports and interfaces again.

