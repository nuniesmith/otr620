"""Validated scenarios with deterministic virtual time."""

import json
from pathlib import Path
from .config import number, percentage
from .sensors import Reading, parse_w1


DEMO = [
    {"temperature_c": 25},
    {"temperature_c": 34},
    {"temperature_c": 35, "led_enabled": True},
    {"temperature_c": 40},
    {"temperature_c": 45},
    {"temperature_c": 34},
    {"temperature_c": 32},
    {"temperature_c": None},
    {"temperature_c": 30},
    {"temperature_c": 30, "age_s": 20},
    {"temperature_c": 30, "fan_mode": "boost"},
    {"temperature_c": 30, "fan_mode": "auto", "led_enabled": False},
]


def load_scenario(path: Path | None = None) -> list[dict]:
    if path is None:
        return [dict(row) for row in DEMO]
    raw = path.read_bytes()
    if len(raw) > 1_048_576:
        raise ValueError("scenario exceeds 1 MiB")
    rows = json.loads(raw)
    if not isinstance(rows, list) or not 1 <= len(rows) <= 10000:
        raise ValueError("scenario must contain 1 to 10000 rows")
    allowed = {"temperature_c", "w1_text", "error", "age_s", "fan_mode", "led_enabled", "led_brightness_pct"}
    for i, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) - allowed:
            raise ValueError(f"scenario row {i}: invalid keys or row type")
        sources = {"temperature_c", "w1_text", "error"} & row.keys()
        if len(sources) != 1:
            raise ValueError(f"scenario row {i}: supply exactly one temperature_c, w1_text or error")
        if row.get("temperature_c") is not None:
            number(row["temperature_c"], "temperature_c")
        if "w1_text" in row and not isinstance(row["w1_text"], str):
            raise ValueError("w1_text must be a string")
        if "error" in row and (not isinstance(row["error"], str) or not row["error"].strip()):
            raise ValueError("error must be a nonempty string")
        if number(row.get("age_s", 0), "age_s") < 0:
            raise ValueError("age_s must not be negative")
        if "fan_mode" in row and row["fan_mode"] not in ("auto", "boost"):
            raise ValueError("fan_mode must be auto or boost")
        if "led_enabled" in row and not isinstance(row["led_enabled"], bool):
            raise ValueError("led_enabled must be a boolean")
        if "led_brightness_pct" in row:
            percentage(row["led_brightness_pct"], "led_brightness_pct")
    return rows


def reading_from_row(row: dict, sensor_id: str, now_s: float) -> Reading | None:
    sampled = now_s - row.get("age_s", 0)
    if "w1_text" in row:
        return parse_w1(row["w1_text"], sensor_id, sampled)
    if "error" in row:
        return Reading(sensor_id, None, sampled, row["error"])
    if row["temperature_c"] is None:
        return None
    return Reading(sensor_id, row["temperature_c"], sampled)
