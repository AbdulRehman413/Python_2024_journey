time = int(input("Enter the time (1-12): "))
region = input("Enter the region (AM/PM): ").strip().upper()

# Check the time and region to determine the greeting
if region == "AM":
    if time in range(1, 12):
        print("Good morning sir")
    elif time == 12:
        print("Good noon sir")  # Special case for 12 AM
elif region == "PM":
    if time in range(1, 6):
        print("Good afternoon sir")
    elif time in range(7, 12):
        print("Good evening sir")
    elif time == 12:
        print("Good noon sir")  # Special case for 12 PM
    elif time == 7 or time == 8 or time == 9 or time == 10 or time == 11:
        print("Good night sir")
else:
    print("Invalid region. Please enter AM or PM.")