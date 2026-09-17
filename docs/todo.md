# OTR620 tasks

[Current design](README.md) · [Conversation archive](chats.md)

Baseline: **V3.1 fit prototype**, September 17, 2026. Checked items reflect work recorded in the session. Unchecked items have no recorded completion. Electrical values and unmeasured fit dimensions are provisional. No deadlines have been agreed.

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

## 1. Truck and accessory tests — next work

Goal: verify the truck and accessories before committing to the full print; the GPS is not required for these steps.

- [ ] Confirm filament, nozzle diameter and slicer profile for the Ender 3 Neo.
- [ ] Select the final dashboard material based on printer capability and heat performance; keep mockup and final-material results distinct.
- [ ] Inspect each test in the slicer at 100% scale; check clips, exclusion zones, purge lines, support footprint and brim clearance.
- [ ] Print `truck_fit_frame.stl`; check opening, corner radii, floor ridges and trim behind the wider mounting tabs.
- [ ] Print `fit_gauge.stl`; check depth, taper and the top-bar step against the stated 25.4/50.8 mm depths.
- [ ] Determine whether to remove the existing ball mount or revise geometry to clear it.
- [ ] Print `dash_bolt_test.stl`; measure actual dash bolts and confirm head/shank fit, rear access and installation hardware. These are separate from the small M2 faceplate screws.
- [ ] Print `nut_fit_test.stl` and `bolt_cover_test.stl`; compare 4.1/4.3/4.5 mm nut allowances with actual hardware.
- [ ] Verify screw reach and repeated faceplate removal; settle how nuts remain in the open loading slots when screws are absent.
- [ ] Measure rubber thickness including adhesive and its compressed thickness; test `pad_test.stl` with a measured 20 mm block.
- [ ] Test adhesive compatibility with the rubber and chosen print material.
- [ ] Print `accessory_test.stl` with the Latercase installed; measure AirPods case-on width, height and depth, and PopSocket length, width and thickness.
- [ ] Check the shelf reach with a cardboard profile: approximately 80.1 mm forward and 73.9 mm below the cubby.
- [ ] Record photos and measured tight/loose areas, then revise CAD parameters and reprint affected coupons.

Completion criterion: measured truck, hardware, pad and accessory results are recorded; the shelf clears nearby controls and trim.

## 2. GPS verification — when the unit arrives

- [ ] Measure the OTR620 housing and compare it with the 152.4 × 86.4 × 18 mm stand-in.
- [ ] Photograph the rear square-on with a ruler; locate USB-C, speaker, microphone, power button and microSD access.
- [ ] Measure the plastic bezel and verify the 1.2 mm faceplate overlap stays clear of display glass.
- [ ] Confirm the required rubber compression and closure stops; avoid clamping the glass or distorting the housing.
- [ ] Choose a replaceable silicone gasket or compatible gasket-maker process; test the 1.2 × 0.6 mm groove. Fully cure formed gasket material away from the GPS.
- [ ] Measure the right-angle cable while plugged in: rear projection, sideways reach, strain-relief envelope and exit direction.
- [ ] Confirm the cable route through or behind the cubby; the current insert uses the nominal full 50.8 mm depth.
- [ ] Revise the USB clearance pocket and add a removable cable-jacket clamp if needed, keeping slack at the connector.
- [ ] Read GPS/adapter labels and verify operating voltage and charging demand with navigation running and a partly discharged battery. Do not adopt 5 V/1 A as a confirmed rating.

Completion criterion: GPS housing, bezel, ports, cable envelope and electrical requirements have been verified with the actual hardware.

## 3. Mechanical assembly and validation

- [ ] Recheck thin sections near tongue channels and rear microphone routing before adding holes, latch roots or electronics mounts.
- [ ] Slice `insert.stl`, `faceplate.stl` and `shelf.stl`; inspect the insert step, nut tabs, tongues, supports and print orientation.
- [ ] Assemble using measured dash hardware and tested M2 fasteners; verify the lower bolts clamp the shelf tongues/L-tabs as intended.
- [ ] Confirm the 176.5 mm tab width and 6.6 mm faceplate projection plus screw heads clear the actual dashboard.
- [ ] Confirm comfortable GPS insertion/removal and repeatable screw/nut service without excessive pad compression.
- [ ] Check AirPods lid opening, retrieval, upward-facing orientation and future charging-cable access.
- [ ] Test steel target or matching magnets against the actual PopSocket before selecting the insert or adhesive.
- [ ] Evaluate AirPods and PopSocket retention; add a strap, latch or retaining feature if tray lips/magnetic attraction are insufficient.
- [ ] Compare rear-speaker sound with and without the return duct; check for muffling and rattles.
- [ ] Verify microphone, controls, SD access, GPS reception and charging while stationary.
- [ ] Evaluate retention, fastener loosening, pad creep and thermal deformation before relying on the assembly during normal driving.
- [ ] Revise and export affected parts; update CAD check results for the revision actually being printed.

## 4. Initial operation — direct GPS power

- [ ] Install the GPS using its supplied power arrangement and secured cable route.
- [ ] Record GPS compartment, cabin and shelf temperatures under representative use, including sunlight exposure.
- [ ] Check sustained navigation and charging for resets, intermittent power or cable strain.
- [ ] Use the measurements to decide whether ventilation or a fan is needed before adding heat-producing accessories.

## 5. Modular power and dim blue lighting

Dependency: verified device requirements and real component dimensions. The session's 5 V/4 A combined target is an allowance, not a finalized design.

- [ ] Select the automotive power source and supported output contract; evaluate the proposed 9 V/3 A USB-C PD architecture.
- [ ] Recalculate load and conversion-loss budgets from selected hardware, including startup demand and continuous operation.
- [ ] Select a rated converter and protected branches; define behavior for unsupported PD contracts, input faults and overloads.
- [ ] Select USB-C input/output hardware with correct source/sink roles, connection detection and advertised current.
- [ ] Keep GPS power independent of Pico software and accessory switching.
- [ ] Draw the wiring schematic and record component ratings, connectors, wiring and protection in a bill of materials.
- [ ] Design a removable electronics carrier, cable channels and accessible service connections around selected components.
- [ ] Select two diffused blue LEDs, one resistor per LED and a front switch for lighting only; finalize a switch boss without weakening the GPS surround.
- [ ] Test `led_carrier.stl`; aim LEDs at an internal surface and keep wiring clear of the sound path.
- [ ] Test brightness at night and adjust resistor values; add dimming only if useful. A capacitor does not set steady LED brightness.
- [ ] Bench-test regulation, combined loads, switching and temperatures before installing accessory electronics.

## 6. AirPods wired charging first

- [ ] Select a suitable shelf USB-C output and short approximately 0.5 ft angled USB-C cable.
- [ ] Check connector access and bend clearance with the Latercase installed and AirPods in the tray.
- [ ] Add a blankable shelf port opening and interchangeable tray backing using actual hardware dimensions.
- [ ] Verify simultaneous GPS and AirPods charging under the expected load and temperature conditions.

## 7. Optional wireless charging

- [ ] Select a complete compatible charging puck and test it through the Latercase before designing its recess.
- [ ] Check alignment, charging stability and temperature with the case at the intended 45° angle.
- [ ] Design a removable puck backing with minimal extra plastic between charger and case.
- [ ] Keep the PopSocket steel target and magnets outside the charging area.
- [ ] Verify the charger cable remains accessible and the holder still supports easy AirPods removal.
- [ ] Compare temperatures with wired charging; retain the wired option if wireless heat or alignment is unacceptable.

## 8. Optional cooling and Pico control

- [ ] Decide from measurements whether active cooling adds value.
- [ ] If needed, design a ventilation path reaching cabin air, preferably separate from the speaker duct.
- [ ] Evaluate lower intake/upper exhaust for passive flow and the proposed top-intake/bottom-exhaust route for forced flow.
- [ ] If using the Noctua NF-A4x10 5V, allow a 40 × 40 mm footprint and verify actual thickness with pads. The existing 39.4 mm sound opening needs revision.
- [ ] Check fan clearance around the GPS, USB elbow, wiring and electronics; measure acoustic interference and airflow after assembly.
- [ ] Select external GPS/charger temperature sensors and define measurement locations and control thresholds.
- [ ] Select a Pico and suitable MOSFETs/load switches; power loads from the distribution hardware rather than GPIO.
- [ ] Implement saved LED brightness and PWM dimming if selected.
- [ ] Implement temperature monitoring, fan hysteresis and charger overtemperature shutdown if those options are installed.
- [ ] Verify sensor-failure, controller-reset and startup behavior while keeping the GPS branch independent.

## 9. Repository and archive maintenance

- [ ] Add these three Markdown files to the intended `otr620` repository. No repository URL or remote has been supplied in this documentation task.
- [ ] Add or organize the current V3.1 source, 12 STLs, hardware image and CAD check report; preserve older revisions as historical.
- [ ] Preserve the original prototype package's printing and assembly notes when integrating this top-level README.
- [ ] Obtain the full Claude export or pasted conversation and append it to `chats.md` under a clearly identified Claude section. The existing file contains only the supplied Claude prompts and available ChatGPT discussion.
- [ ] Add measured dimensions, print settings, fit photos and hardware details as results become available.
- [ ] Track implementation separately from proposed features; update README and tasks after each accepted revision.

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
