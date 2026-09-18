"""An output boundary that deliberately supports simulation only."""

from .controller import Status


class SimulatedOutputs:
    def __init__(self):
        self.last_status: Status | None = None
        self.closed = False

    def apply(self, status: Status) -> None:
        if self.closed:
            raise RuntimeError("simulation outputs are closed")
        self.last_status = status

    def close(self) -> None:
        # There are no physical outputs to switch off. Do not imply a safe
        # fan shutdown policy for the future GPIO driver.
        self.closed = True
