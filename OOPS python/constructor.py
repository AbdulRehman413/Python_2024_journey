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
