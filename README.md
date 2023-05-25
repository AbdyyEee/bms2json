# bms2json 
bms2json is a library built in Python3.11 that implements exporting and importing of `bmsm`, `bmsc`, and `bmss` file formats utilized in games such as Nintendo's Streetpass Mii Plaza. Included is a script as a front-end for preforming those actions.

# Script Usage
```py
python bms.py [-export/-import] [format] [in_path] out_path]
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
source.add(Source())
message.add(Message())
color.add(Color())
```
Reading 
```py
source.read("sample.bmss")
message.read("sample.bmsm")
color.read("sample.bmsc")
```
Writing 
```py
source.write("sample.json")
message.write("sample.json")
color.write("sample.json")
```