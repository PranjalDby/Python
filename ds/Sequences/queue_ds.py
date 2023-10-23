import queue
import timeit
from collections import deque
from typing import Iterable


class Queues[T]:
    def __init__(self, maxsize: int = 0):
        self.maxsize: int = maxsize
        self.front = -1
        self.rear = -1
        self.queue = []
        self.__init(self.queue)

    def __init(self, queue):
        for i in range(self.maxsize):
            queue.insert(i, -1)

    def append_rear(self, data):
        if self.maxsize >= 0:
            if self.rear == -1 and self.front == -1:
                self.front += 1
                self.rear += 1
                self.queue[self.rear] = data

            elif self.rear < self.maxsize-1:
                self.rear += 1
                self.queue[self.rear] = data

    def pop(self) -> T:
        if self.queue == None:
            return
        else:
            if self.front != -1:
                if self.front != -1 and self.front == self.rear:
                    temp = self.queue[self.front]
                    self.queue[self.front] = -1
                    self.rear = self.front = -1
                    return temp

                elif self.front != -1:
                    temp = self.queue[self.front]
                    self.queue[self.front] = -1
                    self.front += 1
                    return temp

    def __repr__(self):
        return str(self.queue)


class CircularQueues[T]:
    def __init__(self, maxsize: int = 0) -> None:
        self.maxsize: int = maxsize
        self.front = -1
        self.rear = -1
        self.queue = list[T]()
        self.__init(self.queue)

    def __init(self, queue):
        for i in range(self.maxsize):
            queue.insert(i, -1)

    def push_at_rear(self, data):
        if self.maxsize > 0:
            if ((self.front == 0 and self.rear == self.maxsize-1) or self.rear == (self.front - 1) % (self.maxsize)):
                # print((self.front == 0 and self.rear == self.maxsize-1))
                # print(self.rear)
                # print("sss",(self.front+1) % (self.maxsize-1))
                # print(self.maxsize -1 )
                # print('queue Full')
                return
            if self.front == -1:
                self.front  = 0
                self.rear = 0

            elif self.front != 0 and self.rear == self.maxsize-1:
                self.rear = 0

            else:
                self.rear += 1
            
            self.queue[self.rear] = data

    def pop(self)->T:
        if self.front == -1:
            return 
        elif self.front == self.rear:
            temp  = self.queue[self.front]
            self.queue[self.front] = -1
            self.front = self.rear = -1
            return temp
        
        elif self.front == self.maxsize-1:
            self.front = 0
        
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = -1
            self.front+=1
            return temp



    def __repr__(self):
        return str(self.queue)


def main():
    c_q = CircularQueues(5)
    c_q.push_at_rear(10)
    c_q.push_at_rear(20)
    c_q.push_at_rear(30)
    c_q.push_at_rear(50)
    c_q.push_at_rear(60)
    # c_q.push_at_rear(160)
    ss = c_q.pop()
    ss = c_q.pop()
    ss = c_q.pop()
    ss = c_q.pop()
    c_q.push_at_rear(102)
    c_q.push_at_rear(110)
    print(c_q)
    print(c_q.front)
    print(ss)


if __name__ == "__main__":
    main()
