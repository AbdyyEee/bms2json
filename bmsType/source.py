from util.Reader import Reader
from util.Writer import Writer


class Source:
    """A class that represents a source entry used by a BMSS file"""
    def __init__(self):
        self.max_width: int = 0
        self.unk1: int = 0
        self.font_path: str = "\\font\\LA4\\cbf_std_edge.bcfnt"
        self.fore_color: str = "nil"
        self.back_color: str = "nil"
        self.x_scale: float = "nil"
        self.y_scale: float = "nil"
        self.x_pos: float = "nil"
        self.y_pos: float = "nil"
        self.unk2: int = "nil"
        self.unk3: bool = False
        self.unk4: int = "nil"
    
    def read(self, reader: Reader):
        self.max_width = int(reader.read_alinged_nstr())
        self.unk1 = int(reader.read_alinged_nstr())
        self.font_path = reader.read_alinged_nstr()
        self.fore_color = reader.read_alinged_nstr()
        self.back_color = reader.read_alinged_nstr()
        self.x_scale = reader.read_alinged_nstr(float)
        self.y_scale = reader.read_alinged_nstr(float)
        self.x_pos = reader.read_alinged_nstr(float)
        self.y_pos = reader.read_alinged_nstr(float)
        self.unk2 = reader.read_alinged_nstr(int)
        self.unk3 = reader.read_alinged_nstr(bool)
        self.unk4 = reader.read_alinged_nstr(int)

    def write(self, writer: Writer):
        writer.write_alinged_nstr(str(self.max_width))
        writer.write_alinged_nstr(str(self.unk1))
        writer.write_alinged_nstr(str(self.font_path))
        writer.write_alinged_nstr(str(self.fore_color))
        writer.write_alinged_nstr(str(self.back_color))
        writer.write_alinged_nstr(str(self.x_scale))
        writer.write_alinged_nstr(str(self.y_scale))
        writer.write_alinged_nstr(str(self.x_pos))
        writer.write_alinged_nstr(str(self.y_pos))
        writer.write_alinged_nstr(str(self.unk2))
        writer.write_alinged_nstr(str(self.unk3))
        writer.write_alinged_nstr(str(self.unk4))