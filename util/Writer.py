import struct
from io import BufferedWriter


class Writer:
    def __init__(self, data: BufferedWriter):
        self.data = data
    
    def skip(self, length: int) -> None:
        self.data.read(length)

    def tell(self) -> int:
        return self.data.tell()
    
    def seek(self, offset, whence = 0) -> int:
        return self.data.seek(offset, whence)

    def write_bytes(self, length: int, data: bytes = b"\x00"):
        self.data.write(data * length)

    def write_alinged_nstr(self, string: str) -> str:
        self.data.write(string.encode("UTF-8"))
        remainder = range(4 - len(string) % 4)
        self.write_bytes(len(remainder))

    def write_uint32(self, num: int) -> None:
        self.data.write(struct.pack(f'<I', num))

    def write_utf16_str(self, string: str):
        self.data.write(b"\xFF\xFE" + string.encode("UTF-16-LE"))
        self.write_bytes(8 - len(string.encode("UTF-16-LE")) % 8)
      
    


