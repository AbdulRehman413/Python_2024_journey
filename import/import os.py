import os

for i in range(0,100):
    os.rename(f"data/day{i+1}" , (f"data/nigga{i+1}"))
import os
folder = os.listdir("data")
print(folder)


for folders in folder:
    print(folders)
    print (os.listdir(f"data/{folders}"))