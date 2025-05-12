class math:

    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a+b
    
a = math(5)
print(a.num)
a.addtonum(7)
print(a.num)
print(math.add(69,69))
print(a.add(69, 69))