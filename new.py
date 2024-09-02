def func1():
    try:
        l = [1,3,4,6,7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0 
    finally:
        print("niga is executed")

x = func1()
print(x)
