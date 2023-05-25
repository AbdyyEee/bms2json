from util.Reader import Reader
from util.Writer import Writer

class Color:
    """A class that represents a color used by a BMSC file"""
    def __init__(self):
        self.color_R: int = 255 
        self.color_G: int = 255
        self.color_B: int = 255
        self.color_A: int = 255 

    def read(self, reader: Reader):
        self.color_R = int(reader.read_alinged_nstr())
        self.color_G = int(reader.read_alinged_nstr())
        self.color_B = int(reader.read_alinged_nstr())
        self.color_A = int(reader.read_alinged_nstr())
    
    def write(self, writer: Writer):
        writer.write_alinged_nstr(str(self.color_R))
        writer.write_alinged_nstr(str(self.color_G))
        writer.write_alinged_nstr(str(self.color_B))
        writer.write_alinged_nstr(str(self.color_A))