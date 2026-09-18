"""Deterministic control decisions independent of displays and networks."""

from dataclasses import asdict, dataclass
from .config import Config, number, percentage
from .sensors import Reading


@dataclass(frozen=True)
class Status:
    elapsed_s: float
    sensor_id: str
    temperature_c: float | None
    sensor_age_s: float | None
    sensor_fault: str | None
    fan_mode: str
    fan_requested_pct: float
    fan_reason: str
    led_enabled: bool
    led_brightness_setting_pct: float
    led_requested_pct: float
    simulated: bool = True
    fan_rpm: int | None = None
    gps_power: bool | None = None

    def to_dict(self) -> dict:
        return asdict(self)


class Controller:
    def __init__(self, config: Config):
        self.config = config
        self._fan_active = False
        self._last_tick: float | None = None

    def step(
        self, reading: Reading | None, now_s: float, *, fan_mode: str = "auto",
        led_enabled: bool | None = None, led_brightness_pct: float | None = None,
    ) -> Status:
        now_s = number(now_s, "now_s")
        if self._last_tick is not None and now_s < self._last_tick:
            raise ValueError("controller time must not move backwards")
        if fan_mode not in ("auto", "boost"):
            raise ValueError("fan_mode must be auto or boost")
        enabled = self.config.led.enabled if led_enabled is None else led_enabled
        if not isinstance(enabled, bool):
            raise ValueError("led_enabled must be a boolean")
        brightness = percentage(
            self.config.led.brightness_pct if led_brightness_pct is None else led_brightness_pct,
            "led_brightness_pct",
        )
        self._last_tick = now_s
        temperature, age, fault = self._inspect(reading, now_s)
        cfg = self.config.fan
        if fault:
            duty, reason = 100.0, "sensor_fault"
            self._fan_active = True
        elif fan_mode == "boost":
            duty, reason = 100.0, "manual_boost"
            self._fan_active = True
        else:
            assert temperature is not None
            if temperature >= cfg.start_c:
                self._fan_active = True
            elif temperature <= cfg.stop_c:
                self._fan_active = False
            if not self._fan_active:
                duty, reason = 0.0, "below_start"
            else:
                fraction = max(0.0, min(1.0, (temperature - cfg.start_c) / (cfg.full_c - cfg.start_c)))
                duty = cfg.min_duty_pct + fraction * (100 - cfg.min_duty_pct)
                reason = "temperature_curve" if temperature >= cfg.start_c else "hysteresis"
        return Status(
            elapsed_s=now_s, sensor_id=self.config.sensor.id,
            temperature_c=temperature, sensor_age_s=age, sensor_fault=fault,
            fan_mode=fan_mode, fan_requested_pct=round(duty, 2), fan_reason=reason,
            led_enabled=enabled, led_brightness_setting_pct=brightness,
            led_requested_pct=brightness if enabled else 0.0,
        )

    def _inspect(self, reading: Reading | None, now_s: float):
        if reading is None:
            return None, None, "missing_sensor"
        if reading.sensor_id != self.config.sensor.id:
            return None, None, "wrong_sensor"
        try:
            sampled = number(reading.sampled_at_s, "sampled_at_s")
        except ValueError:
            return None, None, "invalid_timestamp"
        age = now_s - sampled
        if age < 0:
            return None, None, "future_timestamp"
        if reading.error:
            return None, age, reading.error
        if age > self.config.sensor.stale_after_s:
            return None, age, "stale_sensor"
        try:
            temperature = number(reading.temperature_c, "temperature_c")
        except ValueError:
            return None, age, "invalid_temperature"
        if not self.config.sensor.min_valid_c <= temperature <= self.config.sensor.max_valid_c:
            return None, age, "temperature_out_of_range"
        return temperature, age, None
