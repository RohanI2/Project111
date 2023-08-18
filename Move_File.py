import os
import shutil
source="C:/Users/manoj/OneDrive/Desktop/123"
list_of_files=os.listdir(source)
print(list_of_files)
for i in list_of_files:
    root,ext=os.path.splitext(i)
    print(root)
    print(ext)
