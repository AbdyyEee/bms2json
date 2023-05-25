import json
from util.Reader import Reader
from util.Writer import Writer
from bmxx.header import Header

class bms:
    """A base class for other format's classes to inherit from"""
    def __init__(self):
        self.header: Header = Header()
        self.data: dict = {}

    def to_json(self, filename: str) -> None:
        with open(filename, "w+") as j:
            json.dump(self.data, j, indent=2, default=vars)

    def from_json(self, filename: str, type: any) -> None:
        with open(filename, "r") as j:
            data = json.load(j)

            for label in data:
                new_type = type()
                new_type.__dict__.update(data[label])
                self.data[label] = new_type

    def read(self, filename: str, type: any) -> None:
        file = open(filename, "rb")
        reader: Reader = Reader(file)
        self.header.read(reader)

        entry_count = self.header.entry_count

        while entry_count:
            label: str = reader.read_alinged_nstr()
            file_type = type()
            file_type.read(reader)
            self.data[label] = file_type
            entry_count -= 1
        file.close()

    def write(self, filename: str, string_count: int) -> None:
        with open(filename, "rb+") as f:
            writer: Writer = Writer(f)
            self.header.entry_count = len(self.data)
            self.header.string_count = string_count
            self.header.write(writer)

            for label in self.data:
                writer.write_alinged_nstr(label)
                self.data[label].write(writer)
