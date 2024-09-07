choice = int(input("1 for code and 2 for decode: "))
if choice == 1:
    code  = (input("enter the value:"))
    coding = True
    if coding:
        if (len(code)>=3):
            a1 = "jjd"
            a2 = "sas"
            encoded = a1 + code[1:] + code[0] + a2
            print(encoded)
    else:
            print("your code should be at least 3 letters long")

elif choice == 2:
     code = input("enter the value")
     coding = False
    
     if (len(code)>=3):
        
            code =  code[3:-3] 
            decoded = code[-1] + code[:-1] 
            print(decoded)
     else:
            print("enter correct value to decode")


    
    