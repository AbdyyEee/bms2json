import struct
from io import BufferedReader


class Reader:
    def __init__(self, data: BufferedReader):
        self.data = data

    def skip(self, length: int) -> None:
        self.data.read(length)

    def tell(self) -> int:
        return self.data.tell()

    def seek(self, offset, whence=0) -> int:
        return self.data.seek(offset, whence)

    def seek_until_non_null(self):
        byte = self.data.read(1)
        while byte == b"\x00":
            byte = self.data.read(1)
        self.seek(self.tell() - 1)

    def read_alinged_nstr(self, expected_type=None) -> str:
        string = b""
        while True:
            char = self.data.read(1)
            if char == b"\x00":
                break
            string += char
        string = string.decode("UTF-8")
        self.seek_until_non_null()
        if expected_type is not None:
            if string == "nil":
                return "nil"
            return expected_type(string)

        return string

    def read_utf16_str(self):
        message = b""
        byte = self.data.read(2)
        while True:
            if byte == b"\x00\x00":
                break
            message += byte
            byte = self.data.read(2)

        self.seek_until_non_null()
        return message.decode("UTF-16")

    def read_uint32(self) -> int:
        return struct.unpack(f'<I', self.data.read(4))[0]
