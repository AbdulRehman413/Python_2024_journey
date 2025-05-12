class employee:
    def __init__(self):
        self.__name = "Harry"

a = employee()
print(a._employee__name)
print(a.__dir__())    