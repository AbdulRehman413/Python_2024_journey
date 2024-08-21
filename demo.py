x = int(input("enter the value of x:"))
match x:
    case 1:
        print("x is equal to 544833")
    case 2:
        print("x is 123333")
    case _ if x!=90:
        print("case is not equal to 90")
    case _ if x!=80:
        print("case is not equal to 80")