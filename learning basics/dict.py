dict  = {
   85 : "moiz",
    1: "sodagar",
    48: "abdul rehman",
    43:"abdul sarfraz"
}

print(dict[1])

info = {"name":"abdul Rehman", "age":17, "eligible":"NO"}
print(info)

for key in info.keys():
    print({key},{info[key]})


print(info.items())


ep = {323: 67, 23: 90, 48: 90}
ep2 = {22: 78, 999: 65}


ep.update(ep2)
print("After update:", ep)


if 323 in ep:
    ep.pop(323)
    print("After popping key 323:", ep)
else:
    print("Key 323 not found for pop.")


if ep:
    ep.popitem()
    print("After popitem:", ep)
else:
    print("Dictionary is empty, cannot popitem.")


ep.clear()
print("After clear:", ep)


del ep

