a = input("Enter the value: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("make sure to only use integers and try again")