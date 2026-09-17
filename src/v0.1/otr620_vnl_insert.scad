// Garmin dezl OTR620 flush dash insert
// 2022 Volvo VNL 860 upper dash cubby
//
// Units: mm. Design space: X = across (0 = left edge as the driver sees it),
// Y = up (0 = cubby floor), Z = depth (0 = front face, + goes into the dash).
// The final solids are mirrored once so the printed part has the right handedness.
//
// Export (Linux):
//   openscad -D 'part="insert"'      -o otr620_insert.stl            otr620_vnl_insert.scad
//   openscad -D 'part="fit_frame"'   -o fit_test_1_face_frame.stl    otr620_vnl_insert.scad
//   openscad -D 'part="fit_gauge"'   -o fit_test_2_depth_gauges.stl  otr620_vnl_insert.scad
//   openscad -D 'part="bolt_test"'   -o fit_test_3_bolt_trap.stl     otr620_vnl_insert.scad

part = "insert"; // [insert, fit_frame, fit_gauge, bolt_test, view_insert, view_assembly, view_section]

/* [Cubby: your measurements] */
open_w  = 165.1;  // 6-1/2"  opening width at the front edge
open_h  = 98.4;   // 3-7/8"  floor (front sill) to top of opening
low_h   = 79.4;   // 3-1/8"  floor to underside of the top bar
cubby_d = 50.8;   // 2"      front edge to back wall below the bar
bar_d   = 25.4;   // 1"      front edge to the face of the top bar

/* [Fit and draft] */
fit_side   = 0.30; // gap per side at the front edge
fit_top    = 0.40; // gap at the top edge
bar_gap    = 1.00; // gap to the face of the bar
low_gap    = 0.50; // gap under the bar
draft_side = 4.0;  // each side wall steps in this much at full depth (cubby walls taper)
draft_top  = 1.0;  // ceiling drops this much over the bar depth
draft_low  = 1.5;  // bar underside drops this much toward the back
draft_bot  = 0.5;  // floor rises this much toward the back

/* [GPS: dezl OTR620] */
gps_w   = 152.4;  // 6.0"
gps_h   = 86.4;   // 3.4"
gps_t   = 18.0;   // MEASURE YOUR UNIT (listings say 0.7" / 1.8 cm / 1.9 cm)
gps_r   = 2.0;    // pocket corner radius (device is ~2.3)
fit_gps = 0.5;    // gap per side around the GPS (ASA/PETG shrink eats some of this)
tape_t  = 1.1;    // mounting tape thickness (3M 5952 VHB = 1.1)
chin_h  = 6.6;    // face below the screen, carries the speaker grille

/* [Back-of-GPS features, front view, mm from GPS left edge / top edge] */
pwr   = [22.7, 13.1];  // power key (on the back!)
usb   = [42.6, 75.2];  // USB-C port (on the back, plug points straight back)
sd    = [ 9.1, 70.6];  // microSD slot
mnt   = [76.5, 47.9];  // mount socket recess
mic_x = 100.4;         // microphone hole on the top edge

/* [Bolts] */
bolt_d    = 7.0;           // channel, passes a 1/4" drill bit
head_af   = 10.3;          // hex trap across flats: fits 3/8" and 10 mm heads
seat_back = 12.0;          // plastic under the bolt head, to the back face
bolt_x    = 13.0;          // channel centre from each side of the face
bolt_y    = [14.0, 64.0];  // channel heights above the floor (both below the bar)

/* [Speaker duct, grille, cable] */
win_x    = 24.0;  // duct window starts this far in from each side
win_top  = 46.0;  // top of the duct window (height above floor)
back_t   = 2.0;   // back plate that closes the duct
cable_d  = 20.0;  // cable pass-through in the back plate, behind the USB-C port
bot_wall = 1.7;   // plastic under the grille slots
lip_t    = 1.5;   // plastic between grille slots and GPS
slot_l   = 6.0;
slot_rib = 2.0;
slot_n   = 13;
mic_w    = 8.0;
mic_dp   = 1.2;
pwr_relief_d  = 20.0;
pwr_relief_dp = 3.5;

$fn = 48;

// ---------- derived ----------
FW = open_w - 2*fit_side;
FH = open_h - fit_top;
LH = low_h - low_gap;
D  = cubby_d;
BD = bar_d - bar_gap;
PW = gps_w + 2*fit_gps;
PH = gps_h + 2*fit_gps;
PD = gps_t + tape_t;
px0 = (FW - PW)/2;
py0 = chin_h;
gy0 = bot_wall;
gy1 = py0 - lip_t;
slot_h = gy1 - gy0;
z0  = gps_t + (py0 - gy0) + 0.8;      // duct roof depth at slot bottom (45 deg roof)
pitch = slot_l + slot_rib;
grille_w = slot_n*pitch - slot_rib;
trap_r = head_af/sqrt(3);             // hex circumradius

function gx(fx) = px0 + fit_gps + fx;
function gy(fy) = py0 + fit_gps + gps_h - fy;
function ds(z) = draft_side*z/D;
function db(z) = draft_bot*z/D;

top_wall = (FH - draft_top*PD/BD) - (py0 + PH);
echo(str("face ", FW, " x ", FH, " | pocket ", PW, " x ", PH, " x ", PD,
         " | top wall behind GPS ", top_wall, " | chin ", chin_h,
         " | bolt length under head = ", seat_back, " + dash wall + washer + nut + 2"));
assert(top_wall - mic_dp >= 1.2, "Top wall too thin: reduce chin_h or draft_top");
assert(z0 - (py0 - gy0) >= gps_t, "Grille duct would undercut the GPS");
assert(bolt_x - trap_r >= px0 + 0.5, "Side hex traps must open fully into the pocket");
assert(bolt_y[0] - head_af/2 >= py0 + 0.5, "Lower hex traps must open fully into the pocket");
assert(bolt_x + trap_r <= win_x - 3, "Hex traps too close to the duct window");
assert(bolt_y[1] + trap_r <= LH - draft_low - 3, "Upper bolts too close to the bar");

// ---------- helpers ----------
module rrect(w, h, r) offset(r) offset(-r) square([w, h]);
module slab(z, x0, x1, y0, y1) translate([x0, y0, z]) cube([x1 - x0, y1 - y0, 0.01]);
module to_physical() mirror([0, 0, 1]) children();  // design space is left-handed

// ---------- design-space geometry ----------
module envelope() {
    hull() {  // full-height front section, stops short of the bar
        slab(0, 0, FW, 0, FH);
        slab(BD - 0.01, ds(BD), FW - ds(BD), db(BD), FH - draft_top);
    }
    hull() {  // lower section, full depth
        slab(0, 0, FW, 0, LH);
        slab(D - 0.01, ds(D), FW - ds(D), db(D), LH - draft_low);
    }
}

module gps_pocket()
    translate([px0, py0, -1]) linear_extrude(PD + 1) rrect(PW, PH, gps_r);

module mic_groove()
    translate([gx(mic_x) - mic_w/2, py0 + PH - 0.5, -1]) cube([mic_w, mic_dp + 0.5, PD + 1]);

module duct() {
    // open window behind the GPS: speaker + USB-C + cable space
    translate([win_x, py0 - 0.01, PD - 0.01])
        linear_extrude(D - back_t - PD + 0.01)
            union() {
                rrect(FW - 2*win_x, win_top - py0 + 0.01, 4);
                square([FW - 2*win_x, 5]);
            }
    // passage under the lip, 45 deg roof so it prints without supports
    translate([win_x, 0, 0]) rotate([90, 0, 90])
        linear_extrude(FW - 2*win_x)
            polygon([[gy0, z0], [py0 + 0.02, z0 - (py0 - gy0) - 0.02],
                     [py0 + 0.02, D - back_t], [gy0, D - back_t]]);
    // grille slots through the chin: the sound's way back out the front
    for (i = [0 : slot_n - 1])
        translate([FW/2 - grille_w/2 + i*pitch, gy0, -1])
            linear_extrude(z0 + 1.5)
                hull() {
                    translate([slot_h/2, slot_h/2]) circle(d = slot_h);
                    translate([slot_l - slot_h/2, slot_h/2]) circle(d = slot_h);
                }
}

module reliefs() {
    // power key: nothing may press it
    translate([gx(pwr[0]), gy(pwr[1]), PD - 0.01]) cylinder(d = pwr_relief_d, h = pwr_relief_dp);
    // microSD slot (push-push card would eject if pressed)
    translate([gx(sd[0]) - 7, gy(sd[1]) - 9, PD - 0.01]) cube([14, 18, 2.5]);
    // mount socket recess, in case its rim stands proud
    translate([gx(mnt[0]), gy(mnt[1]), PD - 0.01]) cylinder(r = 29, h = 1.5);
}

module bolts() {
    for (bx = [bolt_x, FW - bolt_x], by = bolt_y) {
        translate([bx, by, PD - 0.01]) cylinder(d = bolt_d, h = D);
        translate([bx, by, PD - 0.01])
            cylinder(r = trap_r, h = D - seat_back - PD + 0.01, $fn = 6); // flats face up/down
    }
}

module cable_hole()
    translate([gx(usb[0]), gy(usb[1]), D - back_t - 1]) cylinder(d = cable_d, h = back_t + 2);

module insert_design()
    difference() {
        envelope();
        gps_pocket();
        mic_groove();
        duct();
        reliefs();
        bolts();
        cable_hole();
    }

module gps_design() {  // simple stand-in for previews
    translate([px0 + fit_gps, py0, 0.02]) {
        color([0.08, 0.08, 0.09]) linear_extrude(gps_t) rrect(gps_w, gps_h, 2.3);
        color([0.15, 0.35, 0.55]) translate([12, 5, -0.05]) cube([gps_w - 17, gps_h - 10, 0.1]);
    }
}

// ---------- printable parts ----------
// Insert: back face down, face up. Enable supports "touching build plate" for the
// strip that sits in front of the bar; everything else is self-supporting.
module print_insert() translate([0, 0, D]) to_physical() insert_design();

// Face frame: front 4 mm of the insert, face down. Checks the opening fit and the GPS fit.
module print_fit_frame()
    translate([0, FH, 0]) mirror([0, 1, 0])
        intersection() {
            insert_design();
            translate([-1, -1, -1]) cube([FW + 2, FH + 2, 5]);
        }

// Depth gauges: two flat 3 mm outlines of the insert's outer shape.
//  SIDE gauge (stand it on edge in the cubby): checks both depths and the bar step.
//  TOP gauge (slide it in flat at mid-height): checks width and the side-wall taper.
// Each should slide in until its FRONT edge is flush with the opening.
gauge_t = 3.0;
module side_profile_2d()  // (depth, height)
    polygon([[0, 0], [0, FH], [BD, FH - draft_top], [BD, LH - draft_low*BD/D],
             [D, LH - draft_low], [D, db(D)]]);
module plan_profile_2d()  // (across, depth)
    polygon([[0, 0], [FW, 0], [FW - ds(D), D], [ds(D), D]]);
module outline_2d(rim = 6) difference() { children(); offset(delta = -rim) children(); }
module gauge_label(s)
    linear_extrude(gauge_t + 0.6) text(s, size = 4.5, font = "DejaVu Sans:style=Bold",
                                       halign = "center", valign = "center");
module print_fit_gauge() {
    // TOP gauge: front edge along Y = 0
    linear_extrude(gauge_t) outline_2d() plan_profile_2d();
    translate([FW/2, 3, 0]) gauge_label("FRONT");
    translate([FW/2, D - 3, 0]) gauge_label("TOP GAUGE");
    // SIDE gauge: X = height above floor, Y = depth, front edge along Y = 0
    translate([0, D + 6, 0]) {
        linear_extrude(gauge_t) outline_2d() mirror([1, -1, 0]) side_profile_2d();
        translate([FH/2, 3, 0]) gauge_label("FRONT");
        translate([(LH - draft_low)/2, D - 3, 0]) gauge_label("SIDE GAUGE");
    }
}

// Bolt trap test: same trap and seat depth as the insert, back face down.
module print_bolt_test() {
    h = D - PD;
    difference() {
        translate([-10, -10, 0]) cube([20, 20, h]);
        translate([0, 0, -1]) cylinder(d = bolt_d, h = h + 2);
        translate([0, 0, seat_back]) cylinder(r = trap_r, h = h, $fn = 6);
    }
}

// ---------- preview views (driver at -Y, Z up) ----------
module view_xf() multmatrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]) children();

if (part == "insert")        print_insert();
if (part == "fit_frame")     print_fit_frame();
if (part == "fit_gauge")     print_fit_gauge();
if (part == "bolt_test")     print_bolt_test();
if (part == "view_insert")   view_xf() color([0.30, 0.31, 0.33]) insert_design();
if (part == "view_assembly") view_xf() { color([0.30, 0.31, 0.33]) insert_design(); gps_design(); }
if (part == "view_section")  view_xf() {
    // cut through a grille slot to show the speaker path
    difference() {
        color([0.30, 0.31, 0.33]) insert_design();
        translate([FW/2 - grille_w/2 + 8*pitch + slot_l/2, -1, -1]) cube([FW, FH + 2, D + 2]);
    }
    difference() {
        gps_design();
        translate([FW/2 - grille_w/2 + 8*pitch + slot_l/2, -1, -1]) cube([FW, FH + 2, D + 2]);
    }
}
