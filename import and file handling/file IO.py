f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()



f = open('myfile.txt', 'a')
print(f)
f.write("niggas in paris")
f.close()

with open('myfile.txt', 'a') as f:
    f.write("hey i am inside u")
    


#for this u need to have another random non working file and have some data in that for it to be working