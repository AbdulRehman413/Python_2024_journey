# class person:
    
#     name = "abdul"
#     occupation = "student"
#     networth = 0 

#     def info(self):
#         print(f"{self.name} is a {self.occupation} with {self.networth} networth")
    
# a = person()
# b = person()
# c = person()
# a.name = "hassan"
# a.occupation = "developer"

# b.name = "umar"
# b.occupation = "unemployed"
# a.info()
# b.info()
# c.info()



# class person:
    
    

#     def __init__(self,n,o):
#         print("i am a person")
#         self.name = n
#         self. occ = o

#     def info(self):
#            print(f"{self.name} is a {self.occ}")
    
# a = person("abdul", "student")
# b = person("hassan", "developer")
# # c = person()

# a.info()
# b.info()
# # c.info()



# def greet(fx):
#     def mfx():
#         print("Good morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx
    
# @greet 
# def hello():
#     print("hello world ")

# hello()


class myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"value is {self._value}")
    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
       
obj = myclass(10)
obj.ten_value = 67
obj.show()
print(obj.ten_value)