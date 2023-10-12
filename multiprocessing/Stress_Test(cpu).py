import multiprocessing
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
def cpu_heater(number):
    return sum(i * i for i in range(number))

def find_sums(lists):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_heater,lists)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(100)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
