# OTR620 truck mount

Parametric Garmin OTR620 mount for the upper dash cubby in a **2022 Volvo VNL 860**, with an external shelf for **AirPods Pro 3 in a Latercase** and an **oval MagSafe PopSocket**.

**Status: V3.1 fit prototype.** CAD checks have been recorded; physical fit, retention and thermal testing are pending. The GPS has not arrived. GPS dimensions, connector positions and electrical requirements remain provisional.

## Documentation

- [README.md](README.md): current design, dimensions, printing sequence and upgrade concepts.
- [chats.md](chats.md): available ChatGPT discussion and user-pasted Claude prompts, including superseded proposals.
- [todo.md](todo.md): completed work, ordered tasks, measurements and release criteria.

This documentation was split from `Garmin_OTR620_Project_Record.docx` on September 17, 2026. The original Claude share was inaccessible; its complete responses are not present. These three files document the existing design package; they do not include the CAD, STL or image assets themselves.

## Start here

1. Use the V3.1 package: `OTR620_VNL_V3_Prototype.zip` (the archive name still says V3).
2. Confirm filament and nozzle, then slice the small truck, hardware and accessory tests at 100% scale for the Ender 3 Neo's stated 220 × 220 mm bed.
3. Record fit results in [todo.md](todo.md) before revising or printing the complete assembly.
4. When the GPS arrives, verify its housing and cable fit and start with its supplied power arrangement. Accessory electronics remain future work.

## Project scope and supplied material

The user supplied a ZIP containing the original v2 OpenSCAD source, two main STL parts, four fit-test STL files and an illustrated preview. Seven images showed the cubby, handwritten measurements, rubber grip tape, the oval PopSocket, a right-angle USB-C cable and an earlier project illustration. The shared Claude URL could not be retrieved. The Claude prompts later pasted by the user are included in the conversation record; the underlying Claude conversation is not represented as reviewed.

The original intent was a flush-looking insert secured to the truck by four bolts, a padded GPS pocket, a return duct that brings sound from the rear speaker out through the front, and a shelf below the cubby. Discussion expanded to removable GPS retention, cable strain relief, low-brightness blue lighting, AirPods charging, temperature sensing and optional active ventilation.

## Current decisions and remaining assumptions

| Item | Current position | Status |
|---|---|---|
| Truck | 2022 Volvo VNL 860 upper dash cubby | User supplied |
| GPS | Garmin OTR620, not yet received | Fit and electrical details pending |
| Printer | Ender 3 Neo with 220 × 220 mm bed | User confirmed |
| Filament and nozzle | Not confirmed | Select before final print settings |
| AirPods | AirPods Pro 3 with Latercase installed | User confirmed; case-on dimensions pending |
| PopSocket | Oval MagSafe base used only for storage | Shape confirmed from photos; dimensions pending |
| Faceplate | Four M2 machine screws with nuts in fixed mounting tabs | Implemented as V3.1 prototype |
| Initial power | One cable directly to the GPS | Staged approach selected |
| Lighting and charging | Removable future additions | Discussed, not electrically implemented |
| Cooling | Reserve space and measure temperature first | No fan installed or mounting geometry finalized |

## Dimensional baseline

The cubby dimensions were supplied as 6.5 inches wide, 3 7/8 inches high at the front, approximately 3 1/8 inches beneath the top bar, 1 inch deep at the top bar and 2 inches deep below it. Draft, corner and floor-ridge assumptions still require the truck gauges.

| Dimension | Current value | Meaning |
|---|---|---|
| Nominal cubby opening | 165.1 × 98.4 mm | User measurement converted to model units |
| Inserted body envelope | 164.5 × 98.0 × 50.8 mm | Width, height and nominal maximum depth |
| GPS stand-in | 152.4 × 86.4 × 18.0 mm | Provisional housing size |
| GPS pocket | 153.8 × 87.8 × 19.0 mm | Based on current pad assumptions |
| Uncompressed side pads | 1.0 mm | Assumed 0.3 mm compression per side |
| V3.1 width over mounting tabs | 176.5 mm | 6 mm projection beyond each side |
| V3.1 faceplate front projection | 6.6 mm plus screw heads | Ahead of nominal GPS face |
| Gasket groove | 1.2 mm wide × 0.6 mm deep | Actual gasket and housing overlap need testing |
| Faceplate housing overlap | 1.2 mm | Must remain clear of display glass |
| AirPods outline test opening | 64.2 × 49.2 mm | Assumed case-on broad-face outline |
| AirPods tray angle and lip | 45 degrees and 8 mm | Front face upward toward driver |
| PopSocket pocket | 58.1 × 91.2 mm | Assumes 56.9 × 90 mm base |
| Steel target ring recess | 55 mm OD, 43 mm ID, 1 mm deep | Placeholder for selected hardware |
| Shelf reach | About 80.1 mm forward and 73.9 mm down | Relative to cubby face and floor |

## Design evolution

The supplied v2 files used a round PopSocket pocket despite the photographed oval accessory. Enabling the legacy oval option triggered an AirPods clearance assertion. The original GPS relied on pad friction, and its cable route was a simple rear hole without strain relief. Estimated rear feature positions, thin local sections and unmodeled cubby ridges were identified as reasons for fit testing.

V3 replaced the accessory shelf layout, introduced an upward-facing AirPods tray, added a screw-fastened gasketed faceplate, enlarged the USB opening and added cable-tie slots. It included a provisional steel-ring recess and a separate LED carrier. V3 initially used screws threaded into the printed plastic and a faceplate about 2.7 mm proud of the GPS.

V3.1 supersedes that fastener design. The user requested metric bolts and nuts for repeatable removal. Because the old side rails were too narrow for robust nut pockets, four tabs were added in front of the dash opening. Four nominal M2 × 6 mm screws enter through the faceplate and engage plain M2 nuts in slots in the fixed insert. The faceplate is now 6.6 mm proud. The shelf geometry is retained from V3.

The nut pockets assume approximately 4 mm across-flats nuts, 1.6 mm thick. The model uses a 4.3 mm pocket and 1.8 mm slot thickness. Coupons provide 4.1, 4.3 and 4.5 mm allowances. Nuts load through an open entry; a removable tape cover was proposed to keep them from sliding out when screws are absent. The slots prevent rotation and axial escape. Thick locking nuts are not a drop-in replacement.

## Mechanical details to retain

Use separated rubber pads on solid support lands, clear of the speaker, microphone, controls, SD slot, bolt wells and USB connector. Grip tape may primarily prevent rattling rather than isolate road vibration. Test its actual thickness, compressibility and adhesive compatibility with the selected print material. Do not assume super glue will hold flexible tape reliably.

The gasket belongs in the removable faceplate and must bear on the plastic housing, never the glass. A replaceable silicone strip offers predictable thickness. If gasket maker is used, form and fully cure it away from the GPS with a product compatible with the printed plastic. The closure stops cannot compensate for a gasket that is too thick.

The rear USB opening combines a rounded 30 × 16 mm cutout with the original 20 mm hole. Cable-tie slots are a provisional strain-relief measure. Leave slack at the plug. A fitted right-angle connector pocket or clamp needs the plugged-in connector envelope and cable-exit direction. The model consumes the nominal cubby depth; access through or around the cubby rear is still needed.

The shelf uses the original tongues and rear L-tabs, clamped by the lower dash bolts. The existing ball mount pictured inside the cubby is not accommodated. The AirPods and PopSocket trays have no positive latches; evaluate retention and add a strap or latch if needed. A steel target ring may work with the PopSocket's existing magnets; test attraction before selecting or gluing hardware.

## Immediate print and fit plan

Print individually at 100 percent scale. All 12 current STL bounding boxes fit the stated 220 × 220 mm bed with 10 mm brim allowance on each side, but slicer exclusion zones, clips, purge lines and support spread still need checking. No machine-specific G-code was created. A 0.4 mm nozzle, 0.20 mm layers and three walls were suggested only as conditional coupon starting settings; the actual nozzle and filament remain unknown.

| Order | File | Test now |
|---|---|---|
| 1 | truck_fit_frame.stl | Opening, corners, floor ridges and surrounding trim under tabs |
| 2 | fit_gauge.stl | Depth, taper and top-bar step |
| 3 | nut_fit_test.stl and bolt_cover_test.stl | Actual nuts, pocket allowance, screw reach and repeat removal |
| 4 | accessory_test.stl | AirPods with Latercase and oval PopSocket outlines |
| 5 | dash_bolt_test.stl | Existing dash bolt head and shank fit |
| 6 | pad_test.stl | Compressed rubber allowance using a measured 20 mm block |
| Later | shelf.stl | Shelf reach, controls clearance, case lid opening and retention |
| After gauges | insert.stl and faceplate.stl | Full mechanical assembly; GPS fit remains provisional |

The shallow truck frame does not test full-depth GPS retention or the complete shelf connection. The USB sample does not establish the plugged-in elbow fit. Print-support needs must be inspected in the slicer, particularly the insert step, mounting tabs and shelf tongues. Do not treat a cool-room fit in a mockup material as validation for dashboard heat.

## Future electronics and charging

The proposed future distribution device uses regulated power and separately protected branches. A Pico would supervise accessories; it would not supply their load current through GPIO. Keep the GPS independent of Pico firmware so accessory-control resets do not intentionally interrupt navigation power.

| Branch | Provisional design allowance |
|---|---|
| GPS | 5 V up to 2 A pending actual verification |
| Compatible AirPods charging module | 5 V up to 1.5 A |
| Dim blue LEDs | Approximately 5 to 20 mA total |
| Pico and optional fan | Reserve approximately 200 mA |
| Combined regulated supply target | Approximately 5 V at 4 A |

These values are design allowances, not confirmed device ratings or measured consumption. The user's proposed 5 V at 1 A GPS requirement was not confirmed in the Garmin manual. Inspect the GPS and adapter labels and measure operation while charging when it arrives. [Garmin OTR620 and OTR720 owner manual](https://www8.garmin.com/manuals/webhelp/GUID-3A374A49-6708-477D-9095-78BB6BD9AA70/EN-US/dezl_OTR620_and_720_OM_%28NA%29_EN-US.pdf)

One expansion candidate is an automotive USB-C PD adapter outside the printed enclosure, a rear USB-C inlet with a controller requesting a supported 9 V at 3 A contract, and a suitably rated converter supplying protected 5 V branches. This is an architecture proposal, not a finished circuit or bill of materials. Select the source and converter together, handle input faults and unsupported contracts, and give USB-C outputs proper connection detection and current advertisement. A nominal 30 W charger does not establish the same power at every output voltage. [TI USB Type-C and Power Delivery guide](https://www.ti.com/lit/slyy109)

For LEDs, start with two diffused blue emitters aimed at an internal surface rather than directly out of the grille. Use a current-limiting resistor for each LED and a front switch controlling only lighting. An illustrative 5 V circuit with an approximately 3 V LED gives about 0.9 mA through 2.2 kilohms or 2 mA through 1 kilohm. These are starting calculations; confirm the actual LED specifications and brightness at night. A capacitor is not the normal brightness-setting component.

AirPods Pro 3 support USB-C and compatible wireless charging methods. [Apple AirPods Pro 3 specifications](https://www.apple.com/airpods-pro/specs/) Start with a shelf USB-C port and a short angled cable, then allow an interchangeable backing for a complete compatible charging puck. Minimize extra printed plastic between the puck and Latercase; keep the PopSocket's metal target outside the charging area. Test charging with the case installed before cutting a permanent recess. The external shelf improves ventilation but does not eliminate charging heat, sunlight or misalignment losses.

## Cooling and control plans

The lower GPS cavity is approximately 29.8 mm deep, and its current sound-window opening is 39.4 mm high. The discussed Noctua NF-A4x10 5V is nominally 40 × 40 × 10 mm; the listed physical thickness reaches 12 mm with pads. The 10 mm designation is not its width. A fan installation would require revised geometry and clearance for air, wiring and the USB elbow. [Noctua NF-A4x10 5V specifications](https://www.noctua.at/en/products/nf-a4x10-5v/specifications)

The user's top-intake and bottom-speaker-exhaust idea can work with forced airflow if the intake reaches cabin air. A separate ventilation path was preferred to limit fan noise in the speaker duct and airflow restriction. Passive lower intake and upper exhaust were suggested where geometry permits. The fan would mainly cool the GPS compartment, not the AirPods charging contact. Air cooling cannot bring a device below incoming air temperature; Garmin's stated charging range is 0 to 45 degrees Celsius. [Garmin OTR620 and OTR720 owner manual](https://www8.garmin.com/manuals/webhelp/GUID-3A374A49-6708-477D-9095-78BB6BD9AA70/EN-US/dezl_OTR620_and_720_OM_%28NA%29_EN-US.pdf)

A Pico has suitable PWM and analogue-input capabilities for dimming and sensors. [Raspberry Pi Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) Proposed tasks are saving LED brightness, reading external sensors near the GPS and charger, enabling accessories through suitable switches or MOSFETs, controlling the fan with hysteresis and disabling wireless charging if its measured temperature becomes excessive. Temperature thresholds, sensor placement, circuitry and firmware have not been selected or implemented.

## Roadmap

Work proceeds through truck and accessory fit tests, GPS verification, mechanical assembly, direct GPS power, lighting and wired charging, then optional wireless charging and Pico/fan control. See [todo.md](todo.md) for the full checklist. No deadlines have been agreed.

## Deliverables and evidence

The latest archive is OTR620_VNL_V3_Prototype.zip, updated internally to V3.1. It contains otr620_vnl_v3_1.scad, README.md, mesh_checks.json, v3_1_hardware.png and 12 STL files: accessory_test, bolt_cover_test, dash_bolt_test, faceplate, fit_gauge, insert, led_carrier, nut_fit_test, pad_test, shelf, truck_fit_frame and usb_test.

The current archive supersedes the original v2 and early V3 faceplate arrangement. The older V3 assembly preview is historical and does not show the new nut tabs. The package file `v3_1_hardware.png` records the revised fastener concept.


All 12 STL files passed the recorded basic mesh-edge and nominal bed-size checks. A faceplate clearance check found no overlap after separating intended contact surfaces slightly. These are CAD checks, not physical fit, strength, fatigue, thermal, acoustic, road-retention or slicer validation.

Original supplied images: IMG_0040.JPEG; IMG_0041.JPEG; IMG_0044.PNG; IMG_0051.JPEG; IMG_0052.JPEG; IMG_0053.JPEG; att.vMFiQBYX14YBz7hegkXZV5H3_4Se0xIlSuxjnK33N3w.jpg. Original archive: 2.zip. Original Claude share: https://claude.ai/share/05fdda11-3323-4d7f-8862-223c79cbf0eb.

## Reference sources used during the session

These are the sources retained from the project record; specifications should be rechecked when selecting final hardware.

- [Garmin OTR620 and OTR720 owner manual](https://www8.garmin.com/manuals/webhelp/GUID-3A374A49-6708-477D-9095-78BB6BD9AA70/EN-US/dezl_OTR620_and_720_OM_%28NA%29_EN-US.pdf)
- [TI USB Type-C and Power Delivery guide](https://www.ti.com/lit/slyy109)
- [Apple AirPods Pro 3 specifications](https://www.apple.com/airpods-pro/specs/)
- [Noctua NF-A4x10 5V specifications](https://www.noctua.at/en/products/nf-a4x10-5v/specifications)
- [Raspberry Pi Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- [Prusa ASA material guidance](https://help.prusa3d.com/article/asa_1809)
