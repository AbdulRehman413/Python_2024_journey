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