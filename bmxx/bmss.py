from bmsType.source import Source
from bmxx.base import bms


class bmss(bms):
    def __init__(self):
        super().__init__()

    def read(self, filename: str):
        super().read(filename, Source)

    def write(self, filename: str):
        super().write(filename, 13)

    def from_json(self, filename: str) -> None:
        super().from_json(filename, Source)
