


import os 

files = os.listdir("folders")
i = 1
for file in  files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"folders/{file}",f"folders/{i}.jpg")
        i = i+1