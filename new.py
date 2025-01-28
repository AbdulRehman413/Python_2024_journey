f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()



f = open('myfile.txt', 'a')
print(f)
f.write("niggas in paris")
f.close()

