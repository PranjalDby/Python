from threading import Thread
from time import sleep
def cube():
    for i in range(100):
        i * i * i
        sleep(0.1)

if __name__ == '__main__':

    threads = []

    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=cube)
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print('end')