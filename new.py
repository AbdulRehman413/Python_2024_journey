ep = {323: 67, 23: 90, 48: 90}
ep2 = {22: 78, 999: 65}
ep.update(ep2)
print(ep)

ep.clear()
print(ep)

ep.pop(323)
print(ep)

ep.popitem()
print(ep)

del ep
print(ep)

