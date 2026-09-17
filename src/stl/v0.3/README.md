# Garmin OTR620 / Volvo VNL 860 — V3.1 truck-fit prototype

Designed around your stated 220 × 220 mm Ender 3 Neo bed. GPS is not yet available, so this revision prioritizes the truck opening, accessory fit and reusable faceplate hardware. All dimensions are mm. Import at 100% and center each file on the bed. The GPS opening, rear feature positions, gasket compression and cable elbow fit remain provisional.

## Faceplate hardware — changed from V3

Four M2 × 6 mm machine screws enter from the front and thread into plain M2 hex nuts held in side-loading slots in the fixed insert. There are no printed screw threads. The nut sits behind the removable faceplate in a mounting tab; it stays with the insert when you remove the faceplate.

The design assumes nuts about 4 mm across flats and 1.6 mm thick. Do not substitute thicker locking nuts without changing the pocket. Print the nut and bolt-cover coupons with your actual hardware first. The main slot is 4.3 mm across flats and 1.8 mm thick. The three coupon slots are 4.1 / 4.3 / 4.5 mm from left to right, viewed with their entries at the top. Cover the open entry with removable tape after inserting the nut so it cannot slide out while the screw is absent. The slot walls prevent spinning; front and back walls retain the nut axially.

Start with pan-head or button-head screws with heads no larger than about 4 mm. Length is measured beneath the head. A nominal 6 mm screw passes through the 2.4 mm faceplate and 2 mm front bearing wall, leaving about 1.6 mm for nut engagement. Check the actual screw tip and nut using the coupons. Do not add washers or change screw length without rechecking engagement and rear clearance. Tighten gently; metal threads improve serviceability but do not make the surrounding print immune to crushing or creep.

The old side rails were too narrow for reliable nut pockets. Four small front tabs now project 6 mm beyond each side of the cubby opening. The inserted body stays 164.5 mm wide; tab/faceplate width is 176.5 mm. The tabs remain in front of the opening, but need clear, reasonably flat trim behind them. The faceplate front is 6.6 mm ahead of the nominal GPS face, plus screw heads. A rear return brings the gasket back to within 0.3 mm of the original GPS plane. This is a raised retainer, not a flush faceplate.

## Print now, without the GPS

1. **truck_fit_frame.stl** — 4 mm-deep front slice plus the new tabs. Check opening width/height, corners, floor ridges and clearance over the surrounding trim. This cannot validate the whole 50.8 mm depth.
2. **fit_gauge.stl** — two thin gauges for depth/taper and the 25.4 mm top-bar step. Check the actual floor ridges and corner fillets too. Remove the pictured existing ball mount before testing.
3. **nut_fit_test.stl** plus **bolt_cover_test.stl** — choose nut-pocket allowance, check M2 × 6 screw reach and repeated removal. These are small handling prototypes, not load tests.
4. **accessory_test.stl** — two outlines: oval PopSocket and the broad front/back outline of the AirPods Pro 3 with Latercase still installed. The AirPods opening is 64.2 × 49.2 mm with 7 mm corner radii; this is an assumption, not a measured Latercase specification. Do not force the case into the print.
5. **dash_bolt_test.stl** — check your existing nominal 1/4-inch shank / 3/8-inch hex-head dash bolts. This hardware is separate from the M2 faceplate screws. The head pocket is 9.9 mm across flats and through-hole 7 mm.
6. **pad_test.stl** — optional rubber test. Openings are 21.0 / 21.4 / 21.8 mm left-to-right. Test with a measured 20 mm-wide block plus your two pad strips, corresponding to compressed pad thicknesses of 0.5 / 0.7 / 0.9 mm per side.

After the truck gauges and accessory outline fit, **shelf.stl** can check the actual shelf position, AirPods angle and interference below the cubby. A cardboard profile first is cheaper: the shelf extends about 80.1 mm forward of the cubby face and 73.9 mm below its floor. The 45-degree tray presents the AirPods broad front face upward toward you. Its lip is 8 mm high with a lower charging/finger notch. Check lid opening, removal and retention with the real case.

**insert.stl** and **faceplate.stl** are included as provisional full parts. Defer the full insert until the truck gauges pass; defer final GPS retention decisions until the unit arrives. **usb_test.stl** and **led_carrier.stl** remain optional provisional samples.

## Ender 3 Neo starting setup

Use your installed nozzle and filament profile. If using a 0.4 mm nozzle, a practical starting point for the dimension coupons is 0.20 mm layers and 3 walls, with 4 top/bottom layers. Inspect actual small-hole toolpaths. Nut coupons are intended to bridge their short slots without internal supports; supports inside the nut pockets would be difficult to remove.

Center and print the large parts individually. All supplied STL XY bounding boxes, including 10 mm brim allowance on every side, fit inside the stated 220 × 220 mm bed. Keep brims/supports clear of bed clips, purge lines and slicer exclusion zones. No machine-specific G-code is supplied. No nozzle or filament type has been assumed as confirmed.

For the main insert, use its exported back-down orientation and review support for the upper step and external tabs. For the shelf, review support for the tongues and overhangs; a brim may help its narrow initial contact. The faceplate exports with its front on the bed and gasket return upward. The truck-fit frame may need support below projecting tabs. Verify those regions in the slicer before printing.

PLA can be used for a dimensional trial, but passing a cool-room fit does not validate a dashboard material. The filament for the installed part remains undecided. Recheck nut fit with the final material.

## Existing design retained

- Cubby envelope 164.5 × 98 × 50.8 mm, with stepped top and tapered sides, derived from your earlier measurements.
- Front sound grille and rear-to-front speaker duct.
- 1 mm uncompressed pad assumption and 0.3 mm side compression. Use small separated pads, clear of speaker, microphone, controls and ports. Adhesive must suit both rubber and print; do not assume super glue works on the flexible grip tape. Never glue the GPS in for these tests.
- Gasket channel 1.2 mm wide × 0.6 mm deep. Housing overlap 1.2 mm remains unverified. Use a separate strip or fully cure any compatible gasket compound in the removed faceplate before assembly; never clamp onto display glass.
- Rear USB opening combines a 30 × 16 mm rounded cutout and the original 20 mm circular hole. Cable-tie slots provide a starting point for jacket strain relief. Leave slack at the connector. No fitted elbow clamp yet.
- Oval PopSocket pocket assumes a 56.9 × 90 mm base with 1.2 mm total clearance. A steel target-ring recess assumes OD 55 / ID 43 / depth 1 mm; measure an actual suitable ring before finalizing it. This area does not charge anything.
- Shelf tongues and rear L-tabs are clamped by the two lower dash bolts. Full assembly is required to test that connection; the shallow truck frame does not reproduce it.
- LED carrier holes are 3.3 mm for nominal 3 mm LEDs. No installed LED location, switch opening, USB-C distribution board or wireless charger is finalized. Two 3.2 mm holes 20 mm apart remain at the shelf bottom for a future bracket.

## Assembly after measurements are confirmed

Fit the nuts from the top of each tab before installing the bracket; temporarily cover their entries. Fit shelf tongues, route the cable, and bolt the insert to the dash with appropriate backing washers/plate and locking hardware. Check what is behind drill locations and avoid crushing dash plastic. The model consumes the nominal cubby depth, so rear cable access is still needed through/around the cubby.

Place tested rubber pads, then the GPS. Fit the faceplate and its gasket and tighten the four small machine screws gently. The tabs serve as closure stops, but they cannot compensate for excessive gasket thickness or wrong GPS thickness. Confirm no pressure on glass, no obstructed microphone/speaker, charging, reception and access for removal. The accessory trays do not have positive latches; add a latch/strap if fit and magnetic hold are insufficient.

## Editable source and export

Open **otr620_vnl_v3_1.scad**. It defaults to an assembly preview with approximate devices. Legacy v2/v3 helpers remain at the beginning for traceability; the active V3.1 section is near the end. Use the commands below instead of older export comments. The legacy shelf flag and items_swap do not control the revised shelf. Nut dimensions are nut_af / nut_slot_t; case dimensions ap_w / ap_h / ap_d include the assumed Latercase.

```sh
openscad -D 'part="insert_v3"' -o insert.stl otr620_vnl_v3_1.scad
openscad -D 'part="bezel_v3"' -o faceplate.stl otr620_vnl_v3_1.scad
openscad -D 'part="shelf_v3"' -o shelf.stl otr620_vnl_v3_1.scad
openscad -D 'part="fit_frame"' -o truck_fit_frame.stl otr620_vnl_v3_1.scad
openscad -D 'part="nut_test"' -o nut_fit_test.stl otr620_vnl_v3_1.scad
openscad -D 'part="bolt_cover_test"' -o bolt_cover_test.stl otr620_vnl_v3_1.scad
```

Other part names: fit_gauge, bolt_test (dash bolts), accessory_test, usb_test, pad_test, led_carrier. Re-export all affected STLs after parameter changes. The full assembly preview is not a printable part.

## Send back after testing

Photos of the frame and gauges in the cubby; tight/loose locations and measured gaps; AirPods-with-Latercase fit; exact PopSocket base dimensions; preferred nut coupon; actual nut/screw dimensions; and filament/nozzle used. GPS-dependent changes can wait until it arrives.

Mesh and bed-size checks are recorded separately in mesh_checks.json. These establish basic geometry and nominal bed fit, not slicer compatibility, physical fit or road durability.

## Nominal print sizes (X × Y × Z)

| Part | Size, mm |
|---|---|
| truck_fit_frame.stl | 176.5 × 98.0 × 8.2 |
| insert.stl | 176.5 × 98.0 × 55.0 |
| faceplate.stl | 176.5 × 92.0 × 6.3 |
| shelf.stl | 164.5 × 131.0 × 97.9 |



## Next revision planning

This directory remains the unchanged V3.1 mechanical baseline. The user is currently printing the four v0.2 fit tests; the v0.3 tabs, M2 hardware and oval accessory fit still need their own checks.

The selected future fan is **Noctua NF-A4x20 5V PWM**, four-pin. The selected host is **Raspberry Pi Zero 2 W with Raspberry Pi OS Lite**. Neither component is fitted or modeled by this revision. Use the [Pi setup and v0.4 plan](../../../docs/pi-setup.md) for its envelope, interface, component measurements and ventilation requirements. Do not interpret the earlier 22 mm pocket proposal as verified installation clearance. Create v0.4 after the fit results and actual component dimensions are available.
