choice = int(input("Press 1 for Code and 2 for Decode: "))
if choice == 1:
    code  = (input("Enter the value you want to code: "))
    coding = []
    coding = True
    if coding:
        if (len(code)>=3):
            a1 = "jsd"
            a2 = "san"
            encoded = a1 + code[1:] + code[0] + a2
            print(encoded)
    else:
            print("Your Code should be at least 3 letters long.")

elif choice == 2:
     code = input("Enter the value you want to decode: ")
     coding = False
    
     if (len(code)>=3):
        
            code =  code[3:-3] 
            decoded = code[-1] + code[:-1] 
            print(decoded)
     else:
            print("enter correct value to decode")