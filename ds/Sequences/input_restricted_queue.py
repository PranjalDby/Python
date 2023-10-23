# input restricted Queue and Output restricted queue

class DoublyEndedQueue[T]:
    def __init__(self,maxsize:int=0) -> None:
        self.maxsize = maxsize
        self.front = -1
        self.rear = -1
        self.doublyq:list[T] = self.__init()

    def __init(self)->list[T]:
        dblyq = []
        for i in range(self.maxsize):
            dblyq.insert(i,-1)
        
        return dblyq
    
    def push_front(self,data):
        if self.front == 0 and self.rear == self.maxsize:
            print('Queue Full')
            return
        
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.doublyq[self.front] =data
        
        elif self.front == 0:
            self.front = self.maxsize-1
            self.doublyq[self.front] = data

        else:
            self.front -= 1
            self.doublyq[self.front] = data

    def push_rear(self,data):
        if (self.front == 0 and self.rear == self.maxsize - 1) or self.rear == (self.front - 1) % (self.maxsize):
            return
        elif self.front != 0 and self.rear == self.maxsize:
            self.rear = 0
        elif self.front == -1:
            self.front = self.rear = 0
            self.doublyq[self.rear] = data
        else:
            self.rear += 1
            self.doublyq[self.rear] = data

    def pop_front(self)->T:
        if self.front == -1:
            print('queue_empty')
            return
        elif self.front == self.rear:
            temp = self.doublyq[self.front]
            self.doublyq[self.front] = -1
            self.front = self.rear = -1
            return temp
        else:
            temp = self.doublyq[self.front]
            self.doublyq[self.front] = -1
            self.front += 1
            return temp
    
    def pop_rear(self) -> T:
        if self.front == -1:
            return
        elif self.rear == -1:
            self.rear = self.maxsize-1
            return
        elif self.rear == self.front:
            temp = self.doublyq[self.rear]
            self.doublyq[self.rear] = -1
            self.front = self.rear = -1
        else:
            temp = self.doublyq[self.rear]
            self.doublyq[self.rear] = -1
            self.rear -=1
           
        return temp
    
dblyq = DoublyEndedQueue[int](10)
dblyq.push_front(50)
dblyq.push_rear(30)
print(dblyq.doublyq)