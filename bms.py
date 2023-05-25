import sys
from bmxx.bmsm import bmsm
from bmxx.bmsc import bmsc
from bmxx.bmss import bmss

arguments = sys.argv[1:]
extensions = ["bmsc", "bmss", "bmsm"]

def get_format(format: str):
    match format:
        case "bmsc":
            return bmsc()
        case "bmsm":
            return bmsm()
        case "bmss":
            return bmss()

extension = arguments[1].lower()
in_path = arguments[2]
out_path = arguments[3]

if extension not in extensions:
    raise Exception("You entered an invalid format.")

file = get_format(extension)

match arguments[0]:
    case "-export":
        file.read(in_path)
        file.to_json(out_path)
    case "-import":
        with open(out_path, "rb+") as f:
            f.truncate()
        file.from_json(in_path)
        file.write(out_path)
    case "-new":
        auto_create = open(in_path, "w+")
        auto_create.close()
print(f"Done.")
        
