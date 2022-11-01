import pipe
def cube(num):
    print(num * num * num)
if __name__ == '__main__':
    ls= list(range(10) | pipe.where(lambda x: x%2 == 0))
    ls2 = list(range(10)|pipe.take_while(lambda x : x < 5)|pipe.where(lambda x: x %2 == 0) | pipe.select(lambda x : x * x))
    print(ls2)


   



