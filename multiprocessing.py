from multiprocessing import Process
import os
import time
def square():
    for i in range(100):
        i*i
        time.sleep(0.1)


if __name__ == '__main__':
    process = []
    num_process = os.cpu_count()

    for i in range(num_process):
        p = Process(target=square)
        process.append(p)
    
    print('Process Started')
    for p in process:
        p.start()

    for p in process:
        p.join()

    print('end main')