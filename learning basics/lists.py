l = [6,7,6,6,7,6]
print(l)
print(type(l))

# print(l[0])
# print(l[3])
# print(l[5])


print(l[-4])
print(l[len(l)-3])



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




#  l.append(  ) can be used to add integer , boolean, or string in the list
# l.sort() arrange the list into ascending order
# l.sort(reverse=True) will be arranged into descending order
# l.reverse() just reverse the origional list
# print(l.index(  )) returns the position of the mentioned int or string and represent it with number
# and if multiple int or strings are present , it will only count out the first occurence
# print(l.count(  )) returns how many times a string or int are occuring in the list
# l.insert(two integers ,(one will tell the position, second will be the value to add)), works almost same as append
# but u can choose where to add the value
# l.extend(  ) is used to add 2 lists together , the second list will be add after the first list
