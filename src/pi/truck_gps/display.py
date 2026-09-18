"""Console rendering of shared status; a physical OLED adapter comes later."""

import json
from .controller import Status


def render_json(status: Status) -> str:
    return json.dumps(status.to_dict(), allow_nan=False, sort_keys=True)


def render_text(status: Status) -> str:
    temperature = "--" if status.temperature_c is None else f"{status.temperature_c:.1f}C"
    return (
        f"SIM t={status.elapsed_s:6.1f}s temp={temperature:>6} "
        f"fan-request={status.fan_requested_pct:5.1f}% ({status.fan_reason}) "
        f"led-request={status.led_requested_pct:5.1f}% "
        f"fault={status.sensor_fault or 'none'} rpm=unknown gps-power=unknown"
    )
