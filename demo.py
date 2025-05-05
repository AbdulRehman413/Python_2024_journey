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



class person:
    
    

    def __init__(self,n,o):
        print("i am a person")
        self.name = n
        self. occ = o

    def info(self):
           print(f"{self.name} is a {self.occ}")
    
a = person("abdul", "student")
b = person("hassan", "developer")
# c = person()

a.info()
b.info()
# c.info()

