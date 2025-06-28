import time
def usingfor():
    i = 0
    for i in range(5000):
        print(i)

def usingwhile():
    i = 0
    while i<5000:
        i = i +1
        print(i)

init = time.time()
usingfor()
ti = time.time() - init
init = time.time()
usingwhile()
init = time.time()-init
print(ti)

print(4)
time.sleep(3)
print("this is printed after 3 seconds")



