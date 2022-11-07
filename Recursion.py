from operator import le
import time

def func(num):
    start = time.time()
    if(num == 0):
        return 
    print(num)
    func(num-1)
    end = time.time()
    print(end - start)

def stringrever(str):
    strs = ""
    if(str == ""):
        return
    count = 0
    while(str!=""):
        strs = str[:count]
        print(strs)
        str = str[:count]


stringrever("Pranjal")
    


