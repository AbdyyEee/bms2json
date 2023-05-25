from util.Reader import Reader
from util.Writer import Writer


class Header:
    def __init__(self):
        self.entry_count: int = 0
        self.string_count: int = 0

    def read(self, reader: Reader):
        self.entry_count = reader.read_uint32()
        self.string_count = reader.read_uint32()

    def write(self, writer: Writer):
        writer.write_uint32(self.entry_count)
        writer.write_uint32(self.string_count)
