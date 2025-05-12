class person:
    
    name = "abdul"
    occupation = "student"
    networth = 0 

    def info(self):
        print(f"{self.name} is a {self.occupation} with {self.networth} networth")
    
a = person()
b = person()
c = person()
a.name = "hassan"
a.occupation = "developer"

b.name = "umar"
b.occupation = "unemployed"
a.info()
b.info()
c.info()