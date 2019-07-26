import os
from os import path
import shutil

src = "C:\\Users\\****\\Desktop\\test1\\"
dst = "C:\\Users\\****\\Desktop\\test2\\"

files = [i for i in os.listdir(src) if i.startswith("CTASK") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)