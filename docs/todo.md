# OTR620 & Truck GPS Master Plan

[Current design](README.md) · [Conversation archive](chats.md) · [TomTom API](tomtom-api.md) · [Google Maps API](google-maps-api.md)

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
- [ ] Ensure power wiring route stays clear of the speaker duct and mechanical stress points during faceplate removal.

---

## 5. Telemetry & Web Tracking System

Goal: leverage the in-truck Starlink Wi-Fi network and a private VPN overlay to track physical coordinates and display them on a real-time map at home.

- [ ] Select the controller board: compare Raspberry Pi Zero 2W (supports native Linux, standard Python, full Tailscale client, web hosting) against Pi Pico 2W (lightweight but extremely difficult network stack).
- [ ] Install **Tailscale** on the selected in-cab Pi; verify connection through the truck's Starlink Wi-Fi.
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

## 8. Optional cooling and fan control

- [ ] Decide from measurements whether active cooling adds value.
- [ ] Model the **Noctua NF-A4x20 5V PWM fan** (40 × 40 × 20 mm) mounting spot:
  - Create a **40 × 40 × 22 mm pocket envelope** in the back of the bracket body (inside the ~29.8 mm deep lower cavity).
  - Verify that the 22 mm allowance is used to clear the fan body plus the vibration-damping silicone corner pads.
  - Position mounting bosses/screw points for small M3 fan-mounting screws or pins in the rear wall of the bracket.
- [ ] Design the symmetrical airflow ventilation loop:
  - Add **hot air exhaust vents** along the top of the bracket faceplate/bezel.
  - Programmatically pattern the top exhaust vents to perfectly mirror the geometry of the bottom sound return/intake ducts for balanced aesthetics.
  - Keep the rising exhaust airflow path completely isolated from the separate sound return duct.
- [ ] Establish bottom-to-top airflow: ensure the fan orientation draws fresh air from the bottom intake, channels it up behind the GPS, and expels it out through the top vents.
- [ ] Check fan physical clearance around the GPS housing, the right-angle USB elbow, internal wires, and any auxiliary switches/buttons.
- [ ] Source and wire the **DS18B20 digital 1-Wire temperature sensor**:
  - Secure a waterproof or TO-92 package DS18B20 sensor.
  - Solder a **4.7kΩ pull-up resistor** between VDD (3.3V) and DQ (Data - GPIO 4) lines.
  - Route wires cleanly through the bracket, isolating them from high-vibration spots.
  - Position the sensor tip close to the GPS's upper rear exhaust zone inside the bracket pocket.
- [ ] Connect the **Noctua 4-Pin PWM Fan** directly to the Raspberry Pi:
  - Connect **Pin 1 (Black/GND)** directly to Pi Ground (GND).
  - Connect **Pin 2 (Red/5V)** directly to Pi 5V power (Pin 2 or 4).
  - Connect **Pin 4 (Blue/PWM)** directly to **GPIO 18** (Pin 12) for hardware speed control (no external MOSFET or components needed).
  - *Optional:* Route Pin 3 (Green/Tachometer) to a GPIO pin with a pull-up if software speed reading is required.
- [ ] Implement and test the Software Control System under `src/pi/`:
  - Enable the 1-Wire kernel modules on the Pi (`w1-gpio` and `w1-therm` via `/boot/firmware/config.txt`).
  - Deploy the automatic temperature daemon script to monitor readings via `/sys/bus/w1/devices/`.
  - Configure dynamic PWM boundaries: Quiet start at **35.0°C (30% speed)** ramping up linearly to **100% full throttle at 45.0°C**.
  - Test PWM frequency generation (25kHz) and verify smooth speed ramping under load.
  - Enable the python script as a background system service (`systemd` daemon) that boots automatically with the Pi.

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
  - Install python dependencies: `pip install luma.oled pillow`.
  - Deploy the in-cab display monitor python daemon script under `src/pi/`.
  - Hook up system queries inside the script to fetch the current Starlink Wi-Fi SSID, local IP address, and Tailscale VPN status.
  - Integrate variables from the fan controller and physical buttons threads to dynamically update fan speed percentages and switch statuses (GPS/LEDs) on the screen.
  - Set the script to boot on startup as a persistent `systemd` system service.

---

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
