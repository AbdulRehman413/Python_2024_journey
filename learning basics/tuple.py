tup = (1,56,677,"green")
print(type(tup),tup)
print(tup[0])
print(tup[-2])
print(tup[3])
if 56 in tup:
    print("yes its present")
else:
    print("not present")

    # tuples are unchangable
print(tup[0:])


tup= (4,4,23,32,23,6,6,6,32,2)
res =tup.count(6)
print(res)
res= tup.index(6,5,9)
print(res)

res = len(tup)
print(res)