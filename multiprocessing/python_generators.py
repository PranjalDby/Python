import random


def odd(start,stop):
    for odd in range(start,stop+1,2):
        yield odd

g = odd(3,15)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def start_process(chance):
    __private  = ["Pranjal","Abss","Rohit"]
    ran = random.choice(__private)
    print("Starting Process")
    print('checking Answer')
    if chance != None:
        while True:
            if chance == ran:
                print("Yes You Guessed My name")
                return
            else:
                chance =  (yield)
                print("Wrong")

if __name__ == "__main__":
    while True:
        try:
            answ = str(input("Guess My name: "))
            cr_obj = start_process(answ)
            cr_obj.__next__() #calling corutine object
            cr_obj.send(answ)
        except StopIteration as e:
            cr_obj.close()
            print("Stopped Process")
            break
