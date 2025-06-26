x = [1,2,4,5]
print(dir(x)) # show types of input data and what methods included in it
print(x.__add__)


class person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
        self.version = 1

p = person("john", 23)
print(p.__dict__) # dict shows what input i had in class

print(help(int)) # just a helper or guide to tell about things in python