from util.Reader import Reader
from util.Writer import Writer

class Message:
    """A class that represents a message entry in a BMSM file"""
    def __init__(self):
        self.source_label: str = ""
        self.message: str = ""
        self.x_scale: int = 0
        self.y_scale: int = 0 
        self.secondary_source_label: str = ""

    def read(self, reader: Reader):
        self.source_label = reader.read_alinged_nstr()
        self.message = reader.read_utf16_str()
        self.x_scale = reader.read_alinged_nstr(int)
        self.y_scale = reader.read_alinged_nstr(int)
        self.secondary_source_label = reader.read_alinged_nstr()

    def write(self, writer: Writer):
        writer.write_alinged_nstr(self.source_label)
        writer.write_utf16_str(self.message)
        writer.write_alinged_nstr(str(self.x_scale))
        writer.write_alinged_nstr(str(self.y_scale))
        writer.write_alinged_nstr(self.secondary_source_label)
    
    
        



