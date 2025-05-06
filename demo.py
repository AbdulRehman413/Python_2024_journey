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


# class myclass:
#     def __init__(self, value):    #class value was 10 , updated the value to 67 and in getter it got multiplied by 10 became 6700
#         self._value = value       # then in setter it got divided by 10 
#     def show(self):
#         print(f"value is {self._value}")
#     @property   #getter 
#     def ten_value(self):
#         return 10*self._value
    
#     @ten_value.setter  #setter 
#     def ten_value(self, new_value):
#         self._value = new_value/10
       
# obj = myclass(10)
# obj.ten_value = 67
# obj.show()
# print(obj.ten_value)




class employee:
    def __init__(self , name, id):
        self.name = name
        self.id = id


    def showdetails(self):
        print(f"the name of employee is {self.name} and his id is {self.id}")


class programmer(employee):
    def showlan(self):
        print("The default language is python")

a = employee("rohan Das", 6969)
a.showdetails()
a1 = programmer ("harry", 7777)
a1.showdetails()
a1.showlan()

