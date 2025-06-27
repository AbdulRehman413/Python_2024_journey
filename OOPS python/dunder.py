class employee:
    name = "harry"
    def __len__ (self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    
    def __call__(self):
        print("hey am a programmer")

e = employee()
print(e.name)
print(len(e))
e()