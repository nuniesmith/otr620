"""Timestamped samples and a pure parser for future Linux 1-Wire integration.

No device reads, retries, threads or GPIO imports happen in this module.
"""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Reading:
    sensor_id: str
    temperature_c: float | None
    sampled_at_s: float
    error: str | None = None


def parse_w1(text: str, sensor_id: str, sampled_at_s: float) -> Reading:
    """Parse one captured w1_slave sample; CRC failures never become 0°C."""
    def fault(reason: str) -> Reading:
        return Reading(sensor_id, None, sampled_at_s, reason)

    if not text:
        return fault("missing_sample")
    if len(text) > 4096:
        return fault("oversized_sample")
    lines = text.splitlines()
    if len(lines) != 2:
        return fault("malformed_sample")
    if not lines[0].split() or lines[0].split()[-1] != "YES":
        return fault("crc_error")
    match = re.search(r"(?:^|\s)t=(-?\d{1,7})\s*$", lines[1])
    if not match:
        return fault("malformed_temperature")
    return Reading(sensor_id, int(match.group(1)) / 1000.0, sampled_at_s)
