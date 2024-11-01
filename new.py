year = int(input("enter total days of feburary: "))
if year == 29:
    print("this year is a leap year")
elif year > 29:
    print("feburary doesnt have that many days, input number of days should be 29 or under 29")
else:
    print("this year is not a leap year")
print("An indication of leap year is that the month feburary will have 29 days")
