from bmsType.color import Color
from bmxx.base import bms

class bmsc(bms):
    """A class that represents a binary message color file"""
    def __init__(self):
        super().__init__()

    def read(self, filename: str):
        super().read(filename, Color)

    def write(self, filename: str):
        super().write(filename, 5)

    def from_json(self, filename: str) -> None:
        super().from_json(filename, Color)
