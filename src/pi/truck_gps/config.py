"""Strict TOML settings; reject typos and non-finite control parameters."""

from dataclasses import dataclass, fields
from pathlib import Path
import math
import tomllib


def number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        finite = math.isfinite(value)
    except OverflowError:
        finite = False
    if not finite:
        raise ValueError(f"{name} must be a finite number")
    return float(value)


def percentage(value: object, name: str) -> float:
    value = number(value, name)
    if not 0 <= value <= 100:
        raise ValueError(f"{name} must be between 0 and 100")
    return value


@dataclass(frozen=True)
class FanConfig:
    start_c: float = 35.0
    stop_c: float = 32.0
    full_c: float = 45.0
    min_duty_pct: float = 30.0

    def __post_init__(self):
        for name in ("start_c", "stop_c", "full_c"):
            number(getattr(self, name), f"fan.{name}")
        percentage(self.min_duty_pct, "fan.min_duty_pct")
        if not self.stop_c < self.start_c < self.full_c:
            raise ValueError("fan thresholds must satisfy stop_c < start_c < full_c")
        if self.min_duty_pct == 0:
            raise ValueError("fan.min_duty_pct must be greater than zero")


@dataclass(frozen=True)
class SensorConfig:
    id: str = "gps-compartment"
    stale_after_s: float = 15.0
    min_valid_c: float = -40.0
    max_valid_c: float = 100.0

    def __post_init__(self):
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("sensor.id must be a nonempty string")
        if number(self.stale_after_s, "sensor.stale_after_s") <= 0:
            raise ValueError("sensor.stale_after_s must be positive")
        if number(self.min_valid_c, "sensor.min_valid_c") >= number(
            self.max_valid_c, "sensor.max_valid_c"
        ):
            raise ValueError("sensor.min_valid_c must be below max_valid_c")


@dataclass(frozen=True)
class LedConfig:
    enabled: bool = False
    brightness_pct: float = 5.0

    def __post_init__(self):
        if not isinstance(self.enabled, bool):
            raise ValueError("led.enabled must be true or false")
        percentage(self.brightness_pct, "led.brightness_pct")


@dataclass(frozen=True)
class Config:
    fan: FanConfig = FanConfig()
    sensor: SensorConfig = SensorConfig()
    led: LedConfig = LedConfig()

    def __post_init__(self):
        if not self.sensor.min_valid_c <= self.fan.stop_c < self.fan.full_c <= self.sensor.max_valid_c:
            raise ValueError("fan thresholds must lie within sensor validity limits")


def load_config(path: Path | None = None) -> Config:
    if path is None:
        return Config()
    raw = path.read_bytes()
    if len(raw) > 65536:
        raise ValueError("configuration exceeds 64 KiB")
    data = tomllib.loads(raw.decode("utf-8"))
    constructors = {"fan": FanConfig, "sensor": SensorConfig, "led": LedConfig}
    unknown = set(data) - constructors.keys()
    if unknown:
        raise ValueError(f"unknown configuration sections: {sorted(unknown)}")
    sections = {}
    for name, cls in constructors.items():
        values = data.get(name, {})
        if not isinstance(values, dict):
            raise ValueError(f"{name} must be a TOML table")
        unknown = set(values) - {f.name for f in fields(cls)}
        if unknown:
            raise ValueError(f"unknown {name} settings: {sorted(unknown)}")
        sections[name] = cls(**values)
    return Config(**sections)
