def square(n):
    '''take the value and returns its square'''
    print(n**2)
square(7)
print(square.__doc__)

letter = "my name is {} and i am from {}"
country= "pakistan"
name = "Abdul Rehman"

print(letter.format(name, country))
print(f"my name is {name} and i live in {country}")


price = 49.9999
seller = f"for only {price:.2f} dollars"
print(seller)

print(f"{2*49}")
print(type(seller))