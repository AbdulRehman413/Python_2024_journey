s = {2,2,4,4}
print(s)
print(type(s))

s2 = {"bigga", 27, True , 67, 67}
print(s2)

abdul = set()
print(type(abdul))

for value in s2:
    print(value)


s1 = {1,2,3,3,4}
s2 = {9,99,78,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
c1.intersection_update(c2)
print(c1)


c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
c3 = c1.intersection(c2)
print(c3)


c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
c3 = c1.symmetric_difference(c2)
print(c3)

c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
c3 = c1.difference(c2)
print(c3)

c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
c3 = c1.isdisjoint(c2)
print(c3)

c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul"}
c3 = c1.issuperset(c2)
print(c3)

c1 = {"tokyo", "lahore", "berlin" , "kabul"}
c2 = {"lahore", "kabul" , "delhi", "washington"}
print(c2.issubset(c1))


c = {"lahore", "karachi","kashmir"}
c.add("nigga")

print(c)

c = {"lahore", "karachi", "kashmir"}
c.remove("lahore")

print(c)

c = {"lahore", "karachi", "kashmir"}
item = c.pop()

print(item)

c = {"lahore", "karachi", "kashmir"}


print(c)

c = {"lahore", "karachi", "kashmir"}
c.clear()

print(c)
