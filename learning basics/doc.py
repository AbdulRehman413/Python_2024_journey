def square(n):
    '''take the value and returns its square'''
    print(n**2)
square(7)
print(square.__doc__)

def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)