class employee:

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        
    
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    

string = "abdul-69000"


e = employee.fromstr(string)
print(e.name)
print(e.salary)