from functools import lru_cache
import time 

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5


print(fx(20))
print("done for 20")
print(fx(4))
print("done for 4")
print(fx(23))
print("done for 23")
print(fx(20))
print("done for 20")
print(fx(4))
print("done for 4")
