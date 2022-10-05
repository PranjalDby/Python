from random import randint


def getfileext(filename):
    return filename[filename.index(".") + 1:]
def otp(num):
    return randint(0,num)*10000