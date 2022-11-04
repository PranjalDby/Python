# python is closure object that remebers values in enclosing scopes even they are not present in memory..
from distutils.log import Log
import logging


def outerFunction(text):
    def innerfunc():
        print(text)
    
    return innerfunc

myfunc = outerFunction('Help')
myfunc()
logging.basicConfig(filename='closures.log',level=logging.INFO)
def logger(func):
    def log_fun(*args):
        logging.info('Running "{}" with arguments'.format(func.__name__,args))
        print(func(*args))
    return log_fun

def mul(x, y):
    return x* y

logg = logger(mul)
logg(2,3)