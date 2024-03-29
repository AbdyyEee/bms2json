# bms2json 
bms2json is a library built in Python3.11 that implements exporting and importing of `bmsm`, `bmsc`, and `bmss` file formats utilized in games such as Nintendo's Streetpass Mii Plaza. Included is a script as a front-end for preforming those actions.

# Script Usage
```console
bms [-export/-import] [bmss/bmsc/bmsm] [in_path] [out_path]
```
Export example (bmsm)
```console
bms -export bmsm something.bmsm something.json
```

Import example (bmsm)
```console
bms -import bmsm something.json new_file.bmsm
```

# Class usage 
Creation of a blank file
```py
source = bmss()
message = bmsm()
color = bmsc()
```

Adding of data
```py
from bmxx.color import Color
from bmxx.source import Source
from bmxx.message import Message 

# Adding with default parameters
source.data["test_label"] = Source()
color.data["test_label"] = Color()
message.data["test_label"] = Message()
```
Reading 
```py
source.read("sample.bmss")
message.read("sample.bmsm")
color.read("sample.bmsc")
```
Writing 
```py
source.write("sample.bmss")
message.write("sample.bmsm")
color.write("sample.bmsc")
```

# Resource
https://avsys.xyz/wiki/BMS_(File_Format)#BMS
