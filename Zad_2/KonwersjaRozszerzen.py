import os
from pathlib import Path

path2 = './photos'
for i in range(4):
    file_name = "photo{}.jpg"
    open(os.path.join(path2, file_name.format(i)), 'a').close()
files = os.listdir(path2)
print(files)
for file in files:
    fPath = Path(os.path.join(path2, file))
    fPath.rename(fPath.with_suffix('.png'))
files = os.listdir(path2)
print(files)