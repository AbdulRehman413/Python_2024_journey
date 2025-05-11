time = int(input("enter the time:"))
region = str(input("enter the region (AM/PM ONLY):")).upper().strip()

if region == "AM":
    if time in range (1,12):
        print("Good morning sir")
    elif time == 12:
        print("Good noon sir ")
elif region == "PM":
    if time in range (1,6):
        print("Good afternoon sir")
    elif time == 6:
        print("Good evening sir ")
    elif time in range (7,12):
        print("Good night sir ")
    elif time == 12 :
        print ("good night sir")
else:
    print("enter the correct region and time")



#note : This project represents just a clock that tells u good morning, goood afternoon, good evening , or good night 
#based on the time that you have entered , this is a begineer level code