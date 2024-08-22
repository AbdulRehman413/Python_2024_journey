for i in range(12):
    if (i==10):
        print("skip the iteration")
        continue
    print("5X",i , "=",5*i)


for i in range(12):
    print("5X",i+1, "=",5*(i+1))
    if(i==9):
        break

for i in range(1,101,2):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("mississippi")

for i in(2,3,4,5,6,7,8):
    if(i%2!=0):
        continue
print("mississippi")


i = int(input("enter the number to see its multiplicartion table: "))
for i in range(11):
    for x in range(1,11):
        print(x , "x", i+1, "=", x*(i+1))
        if(i==9):
            break

