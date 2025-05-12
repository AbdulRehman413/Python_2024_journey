class employee:
    companyname = "lenovo"
    noofemployees = 0
    def __init__(self, name):
        self.name = name 
        self.raise_amount = 0.02
        employee.noofemployees +=1

    def showdata(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} consisting of {self.noofemployees} employee is {self.raise_amount}")

a = employee("Harry")
a.raise_amount = 5
a.companyname = "Dell"
a.showdata()
# employee.showdata(a)
b = employee("rohan")
b.raise_amount = 5
b.showdata()