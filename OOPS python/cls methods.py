class employee:
    company = "apple"
    def show(self):
        print(f"The name of the company is {self.company} in which {self.name} works ")

    @classmethod
    def changecompanyname(cls, newcompany):
        cls.company = newcompany


a = employee()
a.name = ("harry")
a.show()
a.changecompanyname("tesla")
a.show()
print(employee.company)