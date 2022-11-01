'''
generatos are function which return the object which is iteratable
'''
import sys
def genartors():
    yield 1
    yield 2
    yield 3

def countdown(start):
    print('start')
    while start > 0 :
        yield start
        start -= 1

def printlist(n):
    num = 0
    while num < n:
        yield num
        num +=1

def fibo(n):
    a,b = 0,1
    while(a<n):
        yield a
        a,b = b,a+b



mygener = (i for i in range(10) if i%2 == 0)
for i in fibo(7):
    print(i)
for i in mygener:
    print(i)






