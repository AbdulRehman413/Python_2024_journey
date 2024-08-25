l = [1,32,554,63]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(32))
l.insert(2,7788)
m = [100,5094,599]
l.extend(m)
j = l + m
print(l)
print(j)