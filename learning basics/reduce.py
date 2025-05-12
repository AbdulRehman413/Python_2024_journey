from functools import reduce

n = [1,2,3,4,5]
sum = lambda x,y: x+y
r = reduce(sum,n)
print(r)