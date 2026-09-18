"""Command line demonstration; hardware mode cannot be enabled."""

import argparse
import logging
from pathlib import Path
import signal
import threading

from .config import load_config, number, percentage
from .controller import Controller
from .display import render_json, render_text
from .hardware import SimulatedOutputs
from .simulation import load_scenario, reading_from_row

LOG = logging.getLogger("truck_gps")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Truck GPS accessory simulation — no hardware outputs")
    parser.add_argument("--mode", choices=["simulate"], default="simulate")
    parser.add_argument("--config", type=Path)
    parser.add_argument("--scenario", type=Path, help="JSON scenario; defaults to the built-in demo")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--fan-mode", choices=["auto", "boost"], default="auto", help="initial mode; scenario events can change it")
    parser.add_argument("--led-brightness", type=float, help="initial setting; does not enable the LEDs")
    parser.add_argument("--led-on", action="store_true", help="initially enable LEDs")
    parser.add_argument("--interval", type=float, default=5.0, help="virtual seconds per sample")
    parser.add_argument("--realtime", action="store_true", help="pace samples in wall-clock time")
    parser.add_argument("--loop", action="store_true", help="repeat scenario; requires --realtime")
    args = parser.parse_args(argv)
    try:
        interval = number(args.interval, "interval")
        if not 0 < interval <= 60:
            raise ValueError("interval must be greater than 0 and at most 60 seconds")
        if args.loop and not args.realtime:
            raise ValueError("--loop requires --realtime")
        config = load_config(args.config)
        rows = load_scenario(args.scenario)
        brightness = percentage(
            config.led.brightness_pct if args.led_brightness is None else args.led_brightness,
            "led brightness",
        )
    except (ValueError, OSError) as error:
        parser.error(str(error))

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    LOG.info("Simulation only: GPIO, fan power and GPS power are not controlled")
    controller = Controller(config)
    outputs = SimulatedOutputs()
    stop = threading.Event()
    old_handlers = {}
    if threading.current_thread() is threading.main_thread():
        for sig in (signal.SIGINT, signal.SIGTERM):
            old_handlers[sig] = signal.signal(sig, lambda *_: stop.set())
    render = render_json if args.format == "json" else render_text
    tick = 0
    mode = args.fan_mode
    enabled = args.led_on or config.led.enabled
    try:
        while not stop.is_set():
            for row in rows:
                if stop.is_set():
                    break
                mode = row.get("fan_mode", mode)
                enabled = row.get("led_enabled", enabled)
                brightness = row.get("led_brightness_pct", brightness)
                now = tick * interval
                status = controller.step(
                    reading_from_row(row, config.sensor.id, now), now,
                    fan_mode=mode, led_enabled=enabled, led_brightness_pct=brightness,
                )
                outputs.apply(status)
                print(render(status), flush=True)
                tick += 1
                if args.realtime:
                    stop.wait(interval)
            if not args.loop:
                break
    finally:
        outputs.close()
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
        LOG.info("Simulation stopped; no physical outputs were changed")
    return 0
