time = int(input("Please enter the current time:"))
region= str(input("enter the region (AM/PM only):")).upper().strip()

if region == "AM":
    if time in range (1,12):
        print("Good morning sir")
    elif time == 12:
        print("Good noon sir ")
elif region == "PM":
    if time in range (12,6):
        print*("Good afternoon sir")
    elif time == 6:
        print("Good evening sir ")
    elif time in range (7,12):
        print("Good night sir ")
    elif time == 12 :
        print ("good night sir")
else:
    print("enter the correct region and time")
