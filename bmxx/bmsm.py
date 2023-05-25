from bmsType.message import Message
from bmxx.base import bms


class bmsm(bms):
    def __init__(self):
        super().__init__()

    def read(self, filename: str):
        super().read(filename, Message)

    def write(self, filename: str):
        super().write(filename, 6)

    def from_json(self, filename: str) -> None:
        super().from_json(filename, Message)
