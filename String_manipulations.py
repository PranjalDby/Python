from itertools import count
from webbrowser import get

from pygame import init


str = 'helloPranjal'
def addtostring(str,char,index):
    list = []
    for i in range(len(str)):
        list.insert(i,str[i])
    # list.insert(index,char)
    for i in range(len(str)-1,index,-1):
        list[i] = list[i-1]
    
    list[index] = char  

    return list

# for(int i>=pos;i)
def getrev(str):
    list = []
    count = len(str)-1
    for i in range(len(str)):
        list.insert(i,str[count])
        count-=1
    return list
        

print(' '.join(addtostring(str,'g',6)))
        

