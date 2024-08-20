num = 18
num = int(input("enter some shit"))
if num<0:
    print("number is negative")
elif num>0:
    if num<=10:
        print("number is bewteen 1-10")
    elif (num>10 and num<=20):
        print("nummber is  bewteen 11-20")
    else:
        print("number is greater than 20")
    print("good")