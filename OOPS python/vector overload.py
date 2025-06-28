class vector:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    

    def __add__(self,x):
        return vector (self.i+ x.i, self.j+ x.j, self.k + x.j)
    
    

v1 = vector(3,6,8)
v2 = vector(7,9,1)
print(v1 +v2)
print(type(v1+v2))
