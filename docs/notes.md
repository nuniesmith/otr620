# This is for raw notes, ideas to be transferred over to the repos docs

need to research how i can use a raspberry pi pico 2W to add to the project to control the blue leds, fan (if needed), power management so i can use a single usb c into the pi, the pi can power the gps, lights, charge the airpods with a usb c connector or wireless charging built into the airpods mount.
the front of the bracket we can add buttons to control the pi for main power, power for the gps, power for the lights, and power for the fan etc. 
I do have wifi in the truck with starlink so the pi can connect to the wifi for playing with it once its installed to add more features, might look into
adding gps tracking for when im driving later on, i should be able to ssh into the pi depending what OS we use, note sure if we can run a ubuntu base OS or not. In the future, would be nice to keep track of km/miles travelled, states/provinces/countries travelled to for the calandar year. Later i might use this gps into to feed into a map and traffic api to get real time traffic updates. I know tomtom has a free api to play with, more live traffic updates are a good thing. The garmin gps is pretty good at making sure i am on the right road with a big truck at 13'6" standard reefer trailers usually.

review the pdf with the tomtom free api starting points, i think for my personal use, it should be enough to play with later on with a pi into this unit.

Go over the pros and cons of having 1 or 2 usb c cables into the back of the bracket. If we have 2, we can power the pi and the gps separately, if we have 1, we can power both with the same usb c cable. The gps doesn't need much power, 5V at 1A so there should be enough power for the pi to power the gps but might add extra failure points.

Google also has a free tier with their maps api, so we could build different map apis and use them on the free tier and also get differet sources for live traffic.

Another idea, with the pi having gps data and tracking it, i would like to setup a physical map of canada and USA at home for the wife, this would have a little truck on the map of where i am in real time. At home, something like a small tv/monitor with another pi to hdmi would work fine i am sure. Since everything has tailscale on it, i am sure the pi pico will have tailscale if possible. Making it easy to using client devices to lookup a webpage over tailscale to view the map with live real-time location of my truck.

update the docs to include the new structure of dirs for this repo and changed the name to truck-gps to be more generic. We can put any pi code under src/pi and stl files for 3d printer code under src/stl.

Review the pdf's under doc and convert them into their own md file, then we can delete the pdf's.



## Current decisions following the Pi review

The raw notes above remain the original ideas. The current selected fan is the **Noctua NF-A4x20 5V PWM**, four-pin. Its mount and ventilation remain v0.4 work pending fit tests and actual hardware dimensions. See [Pi setup and implementation](pi-setup.md) for the verified fan table and review findings.

The selected Linux host is **Raspberry Pi Zero 2 W with Raspberry Pi OS Lite**, confirmed by the user for a full OS and low-level peripheral control. Accessories draw from rated power-distribution hardware, not Pi GPIO. The GPS's suggested 5 V/1 A demand and a live Garmin position interface remain unverified. Begin with direct Garmin power, then bench-test accessory control. The four v0.2 test prints are in progress; v0.4 CAD has not started.
