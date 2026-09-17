# OTR620 & Truck GPS Master Plan

[Current design](../README.md) · [V3.1 print instructions](../src/stl/v0.3/README.md) · [Conversation archive](chats.md) · [TomTom API](tomtom-api.md) · [Google Maps API](google-maps-api.md)

Baseline: **V3.1 fit prototype**, September 17, 2026. Checked items reflect work recorded in the session. Unchecked items have no recorded completion. Electrical values and unmeasured fit dimensions are provisional. No deadlines have been agreed.

---

## Completed design and documentation work

- [x] Review the supplied v2 source, six STL files and seven photos.
- [x] Identify the oval PopSocket mismatch, friction-only GPS retention and missing cable strain relief.
- [x] Create the V3 padded cradle, gasketed removable faceplate, upward-facing 45° AirPods tray and oval PopSocket pocket.
- [x] Enlarge the rear USB opening and add provisional cable-tie slots.
- [x] Update to V3.1 with four M2 × 6 mm screws and plain M2 nuts in the fixed bracket tabs.
- [x] Include nut-fit coupons and truck/accessory fit tests in the 12-STL package.
- [x] Record basic mesh-edge checks and nominal 220 × 220 mm bed checks, including a 10 mm brim allowance per side.
- [x] Record a faceplate clearance check with intended contact surfaces slightly separated.
- [x] Document the staged power, lighting, charging and cooling concepts.
- [x] Create the Word project record and split it into README.md, chats.md and todo.md.
- [x] Convert Google Maps and TomTom API PDF specifications into standard markdown (`docs/google-maps-api.md`, `docs/tomtom-api.md`) and clean up PDFs.
- [x] Restructure and rename repository to `truck-gps` and map future source code to `src/pi/` and 3D printing components to `src/stl/`.

---

## 1. Truck and accessory tests — next work

**In progress:** the user is printing the four v0.2 test files. Do not mark fit validation complete until results are recorded. The v0.3 tab/nut tests remain separate.

Goal: verify the truck and accessories before committing to the full print; the GPS is not required for these steps.

- [ ] Confirm filament, nozzle diameter and slicer profile for the Ender 3 Neo.
- [ ] Select the final dashboard material based on printer capability and heat performance; keep mockup and final-material results distinct.
- [ ] Inspect each test in the slicer at 100% scale; check clips, exclusion zones, purge lines, support footprint and brim clearance.
- [ ] Remeasure opening height from the cubby floor/top of the black front lip to the opening top; record lip height separately from gray trim. The earlier approximately 8 mm discrepancy was a photo estimate.
- [ ] Print `src/stl/v0.3/truck_fit_frame.stl`; check opening, corner radii, floor ridges and trim behind the wider mounting tabs.
- [ ] Print `src/stl/v0.3/fit_gauge.stl`; check depth, taper and the top-bar step against the stated 25.4/50.8 mm depths.
- [ ] Determine whether to remove the existing ball mount or revise geometry to clear it.
- [ ] Print `src/stl/v0.3/dash_bolt_test.stl`; measure actual dash bolts and confirm head/shank fit, rear access and installation hardware. These are separate from the small M2 faceplate screws.
- [ ] Print `src/stl/v0.3/nut_fit_test.stl` and `src/stl/v0.3/bolt_cover_test.stl`; compare 4.1/4.3/4.5 mm nut allowances with actual hardware.
- [ ] Verify screw reach and repeated faceplate removal; settle how nuts remain in the open loading slots when screws are absent.
- [ ] Measure rubber thickness including adhesive and its compressed thickness; test `src/stl/v0.3/pad_test.stl` with a measured 20 mm block.
- [ ] Test adhesive compatibility with the rubber and chosen print material.
- [ ] Print `src/stl/v0.3/accessory_test.stl` with the Latercase installed; measure AirPods case-on width, height and depth, and PopSocket length, width and thickness.
- [ ] Check the shelf reach with a cardboard profile: approximately 80.1 mm forward and 73.9 mm below the cubby.
- [ ] Record photos and measured tight/loose areas, then revise CAD parameters and reprint affected coupons.

---

## 2. GPS verification — when the unit arrives

- [ ] Measure the OTR620 housing and compare it with the 152.4 × 86.4 × 18 mm stand-in; verify the older approximately 2.3 mm device-radius and 2.0 mm pocket-radius assumptions.
- [ ] Verify that the complete GPS/padding arrangement remains ahead of the top bar, including rear features and cable clearance.
- [ ] Photograph the rear square-on with a ruler; locate USB-C, speaker, microphone, power button and microSD access.
- [ ] Measure the plastic bezel and verify the 1.2 mm faceplate overlap stays clear of display glass.
- [ ] Confirm the required rubber compression and closure stops; avoid clamping the glass or distorting the housing.
- [ ] Choose a replaceable silicone gasket or compatible gasket-maker process; test the 1.2 × 0.6 mm groove. Fully cure formed gasket material away from the GPS.
- [ ] Measure the right-angle cable while plugged in: rear projection, sideways reach, strain-relief envelope and exit direction.
- [ ] Resolve the older 20 mm versus 3/4-inch cable-hole wording: 3/4 inch equals 19.05 mm. Size the opening for the actual connector and any selected protection.
- [ ] Confirm the cable route through or behind the cubby; the current insert uses the nominal full 50.8 mm depth.
- [ ] Revise the USB clearance pocket and add a removable cable-jacket clamp if needed, keeping slack at the connector.
- [ ] Read GPS/adapter labels and verify operating voltage and charging demand with navigation running and a partly discharged battery. Do not adopt 5 V/1 A as a confirmed rating.

---

## 3. Mechanical assembly and validation

- [ ] Recheck thin sections near tongue channels and rear microphone routing before adding holes, latch roots or electronics mounts.
- [ ] Slice `src/stl/v0.3/insert.stl`, `src/stl/v0.3/faceplate.stl` and `src/stl/v0.3/shelf.stl`; inspect the insert step, nut tabs, tongues, supports and print orientation.
- [ ] Assemble using measured dash hardware and tested M2 fasteners; verify the lower bolts clamp the shelf tongues/L-tabs as intended.
- [ ] Confirm the 176.5 mm tab width and 6.6 mm faceplate projection plus screw heads clear the actual dashboard.
- [ ] Confirm comfortable GPS insertion/removal and repeatable screw/nut service without excessive pad compression.
- [ ] Check AirPods lid opening, retrieval, upward-facing orientation and future charging-cable access.
- [ ] Compare rear-speaker sound with and without the return duct; check for muffling and rattles.
- [ ] Verify microphone, controls, SD access, GPS reception and charging while stationary.
- [ ] Evaluate retention, fastener loosening, pad creep and thermal deformation before relying on the assembly during normal driving.
- [ ] Revise and export affected parts; update CAD check results for the revision actually being printed.

---

## 4. Power & Front Bracket Switches Planning

- [ ] Finalize power strategy: evaluate Single USB-C PD Input (using 9V or 12V PD contract stepped down to 5V @ 4A with internal buck converter) vs. Dual USB-C Input (independent cables for GPS and auxiliary boards).
- [ ] Design the front switch/button layout on the bracket to house four physical power control toggles:
  1. **Master Power** (isolates the whole system).
  2. **GPS Power** (enables/disables Garmin OTR620 supply).
  3. **Blue LEDs Power** (manual control of ambient bracket lighting).
  4. **Cooling Fan Power** (manual override / auto toggle for compartment fan).
- [ ] Select appropriate panel-mount miniature toggle or tactile push buttons matching the front depth and width clearances.
- [ ] Define controlled shutdown and power-hold hardware before enabling ignition or master power cutoff on the Linux Pi.
- [ ] Recalculate combined power demand with the selected Pi and all peripherals; the previous 5 V/4 A allowance is not a verified system rating.
- [ ] Keep initial Garmin power separate and prevent accessory/controller resets from interrupting it.
- [ ] Ensure power wiring route stays clear of the speaker duct and mechanical stress points during faceplate removal.

---

## 5. Telemetry & Web Tracking System

Goal: leverage the in-truck Starlink Wi-Fi network and a private VPN overlay to track physical coordinates and display them on a real-time map at home.

- [x] Select **Raspberry Pi Zero 2 W with Raspberry Pi OS Lite** for Linux services plus local peripheral control.
- [ ] Select and verify the board/OS-specific GPIO and hardware PWM backend; configure I²C and 1-Wire for the chosen peripherals.
- [ ] Install **Tailscale** on the selected in-cab Pi; verify connection through the truck's Starlink Wi-Fi.
- [ ] Select and bench-test a GNSS receiver or verify a usable live Garmin interface; do not assume the OTR620 exports NMEA.
- [ ] Write a telemetry background service under `src/pi/` to:
  * Read NMEA GPS data from a connected GPS receiver module.
  * Keep track of cumulative km/miles travelled for the calendar year.
  * Maintain a local JSON database logging states, provinces, and countries visited.
- [ ] Develop a lightweight web dashboard under `src/pi/` (using Python FastAPI/Flask) that:
  * Serves a real-time interactive map showing the truck's current position.
  * Connects to map and traffic engines on free tiers (see [docs/tomtom-api.md](tomtom-api.md) and [docs/google-maps-api.md](google-maps-api.md)).
  * Overlays real-time traffic updates from TomTom Orbis Traffic API on the route.
- [ ] Setup the Home Display System:
  * Configure a secondary Raspberry Pi connected via HDMI to a television or small monitor at home.
  * Install Tailscale on the Home Pi.
  * Configure the Home Pi to boot directly into a browser loading the in-cab Pi's private Tailscale IP webpage (e.g., `http://100.x.y.z/map`).
  * Verify live telemetry reporting and automatic page refreshes.

---

## 6. Modular lighting and wired charging

- [ ] Select two diffused blue LEDs, one resistor per LED, and wire them to the dedicated front button on the faceplate.
- [ ] Test `src/stl/v0.3/led_carrier.stl`; aim LEDs at an internal surface and keep wiring clear of the sound path.
- [ ] Select a suitable shelf USB-C output and short approximately 0.5 ft angled USB-C cable for wired AirPods charging.
- [ ] Check connector access and bend clearance with the Latercase installed and AirPods in the tray.
- [ ] Verify simultaneous GPS and AirPods charging under the expected load and temperature conditions.

---

## 7. Optional wireless charging

- [ ] Select a complete compatible charging puck and test it through the Latercase before designing its recess in the shelf.
- [ ] Check alignment, charging stability and temperature with the case at the intended 45° angle.
- [ ] Design a removable puck backing with minimal extra plastic between charger and case.
- [ ] Verify the charger cable remains accessible and the holder still supports easy AirPods removal.

---

## 8. Selected fan and thermal control

- [x] Select the **Noctua NF-A4x20 5V PWM**, four-pin fan, per the user's preference.
- [ ] Measure the actual fan and verify the [manufacturer dimensions and connection plan](pi-setup.md#selected-fan-and-proposed-interface).
- [ ] Design a removable v0.4 mount with clearance beyond the padded fan envelope, including wiring, fasteners and airflow. Do not assume a 22 mm pocket is sufficient.
- [ ] Verify mounting hardware and the complete fit against the GPS, USB elbow, controller and current cavity.
- [ ] Add top exhaust and lower intake vents with a separate path from the sound duct; check cabin-air access and acoustic effects.
- [ ] Select and identify the DS18B20 sensors; verify power, pull-ups, placement and cable routing.
- [ ] Implement bounded reads, CRC/format validation, stale-data detection and sensor-fault reporting.
- [ ] Choose a hardware PWM backend compatible with the selected Pi/OS and verify 25 kHz timing under load. `RPi.GPIO.PWM()` is not hardware PWM.
- [ ] Replace the previous direct-wiring assumption with a verified Pi-compatible PWM interface and protected fan power branch; confirm connector pin numbering.
- [ ] Configure hysteresis, startup/minimum duty and manual override. Treat the earlier 35–45°C ramp as a provisional bench setting.
- [ ] Test sensor disconnects, a stuck/crashed output, reboot and supply loss. Software requesting full cooling cannot guarantee cooling after loss of power or control hardware.
- [ ] Add optional tach feedback; distinguish requested duty from measured speed.
- [ ] Package the controller with simulation mode, configuration and service management using the [Pi implementation plan](pi-setup.md).

---

## 9. Status Display & Dashboard HUD (I2C OLED)

- [ ] Select and size the **SSD1306/SH1106 I2C OLED display**:
  - Choose between a 0.96" (smaller, standard) or 1.3" (highly readable) 128x64 display panel.
  - Verify that the display uses standard 4-pin I2C connectors (VCC, GND, SCL, SDA).
- [ ] Model the **display bezel & mount** on the bracket front:
  - Create a precise rectangular cutout on the front faceplate for the OLED screen area.
  - Design internal mounting points (screw bosses or slide-in clips) on the rear of the faceplate to secure the display securely against the window.
  - Route the I2C wires cleanly behind the display to prevent interference with the sound duct or AirPods tray.
- [ ] Wire the screen to the Pi:
  - Connect **VCC** directly to **Pi 3.3V (Pin 1)** to match logic levels.
  - Connect **GND** directly to **Pi Ground (Pin 9)**.
  - Connect **SDA** to **GPIO 2 (Pin 3)** and **SCL** to **GPIO 3 (Pin 5)**.
- [ ] Configure and test the Display Software on the Pi OS:
  - Enable the I2C interface via `sudo raspi-config` or adding `dtparam=i2c_arm=on` to `/boot/firmware/config.txt`.
  - Verify address detection via `i2cdetect -y 1` (default address should be `0x3C` or `0x3D`).
  - Install tested dependencies in the application virtual environment; select the driver for the actual OLED controller.
  - Deploy the in-cab display monitor python daemon script under `src/pi/`.
  - Hook up system queries inside the script to fetch the current Starlink Wi-Fi SSID, local IP address, and Tailscale VPN status.
  - Integrate variables from the fan controller and physical buttons threads to dynamically update fan speed percentages and switch statuses (GPS/LEDs) on the screen.
  - Report actual shared state; do not use fixed fan/switch values or label Pi CPU temperature as compartment temperature.
  - Bound network queries and keep display faults independent of fan control.
  - Set the script to boot on startup as a persistent `systemd` system service.

---

## 10. Repository and archive maintenance

- [x] Confirm access to [nuniesmith/truck-gps](https://github.com/nuniesmith/truck-gps) through the GitHub connection.
- [x] Verify the three model directories under `src/stl/` and the V3.1 source, 12 STLs, hardware image and mesh report under `src/stl/v0.3/`.
- [x] Preserve the supplied Claude v0.1/v0.2 responses and available ChatGPT discussion in `docs/chats.md`.
- [x] Preserve the newer telemetry, cooling and OLED plans while reconciling documentation links and current session paths.
- [ ] Implement controller software under `src/pi/` when development starts; this remains a planned directory.
- [ ] If any original Claude prompts, code blocks or turns are missing from the supplied text, append them with their session labels.
- [ ] Update the mechanical source, exported files and print notes together after measured fit changes.

## 11. v0.4 preparation after test prints

- [ ] Record all four v0.2 fit results and photograph interference points; measure the floor-lip reference, corners, taper and shelf clearance.
- [ ] Validate the v0.3 front tabs and M2 coupons plus the oval PopSocket geometry.
- [ ] Confirm actual Pi, fan, OLED, buttons, power hardware and cable envelopes before fixing cutouts.
- [ ] Create `src/stl/v0.4/` from the accepted dimensions, preserving prior revisions.
- [ ] Add a removable electronics carrier, fan bracket, separate vents, serviceable wiring and modular display/switch openings.
- [ ] Keep GPS-dependent fits provisional until the device arrives; validate local coupons before the complete assembly.

## Fit result record

Copy this table for each test or revision. Blank cells indicate information still to record.

| Field | Result |
|---|---|
| Date / CAD revision / test part | |
| Printer / filament / nozzle | |
| Layer height / walls / orientation / supports | |
| Actual hardware or accessory used | |
| Measured dimensions / fit gaps | |
| Tight or interfering locations | |
| Photos / observations | |
| Required CAD change | |
| Retest outcome | |

