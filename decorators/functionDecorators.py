from time import sleep


def squareOf(func):
    def getsqr():
        print('calculating square...')
        sleep(2)
        print('calculating sqr Done.')
        num = func()
        return num * num
    return getsqr

def cube(func):
    def inner():
        print('calculating cube ..')
        sleep(2)
        print('cube Cal Done.')
        res= func()
        return res * res * res
    return inner

def getCube(num):
    return num * num * num
@squareOf
@cube
def num():
    return 10

print(num())



