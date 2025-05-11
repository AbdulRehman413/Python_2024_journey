
print("wasup")
import os

for i in range(0,100):
    os.rename(f"data/day{i+1}" , (f"data/nigga{i+1}"))
import os
folder = os.listdir("data")
print(folder)


for folders in folder:
    print(folders)
    print (os.listdir(f"data/{folders}"))


#create a folder in local disc C and name it anything, then open that folder with vs code and write this code there 
#this code will make 100 new folders in that folder