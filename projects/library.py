class library:
    noofbooks = 0
    def __init__(self, name):       
        self.name = name
        library.noofbooks +=1

    def showbooks(self):
        print(f"the books named {self.name} are {self.noofbooks} in this library")

a = library("atomic habits")
# a.noofbooks = 7
a.showbooks()
b = library("The 5AM club")
# b.noofbooks = 18
b.showbooks()
    