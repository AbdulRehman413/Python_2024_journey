class person:
    
    name = "abdul"
    occupation = "student"
    networth = 0 

    def info(self):
        print(f"{self.name} is a {self.occupation} with {self.networth} networth")
    
a = person()
a.name = "hassan"
a.occupation = "developer"
a.info()