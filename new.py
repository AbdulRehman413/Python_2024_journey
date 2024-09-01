for i in range(8):
    print(i)
    if i == 6:
        break
else:
    print("nah")

i = 0
while i<7:
    print(i)
    i = i+1
else:
    print("nah")

for i in range(5):
    print("iteration no {} in for loop".format(i+1))
else:
    print("else block in loop")