from collections import deque
from array import array
# properties of deque

"""
dequeue is thread safe double ended queue
"""

dq = deque(range(1,10),maxlen=10)
print(dq)
elem = dq.popleft()
print(dq,elem)

# deque implementation
queue = array('l',[0])
size = 10
def form_queue(queue,size):
    for i in range(1,size):
        queue.insert(i-1,-1)
        if i == size-1:
            queue[i] = -1


class Queues[T]:
    def __init__(self:list[T],size:int) -> None:
        self.size = size
        self.capcity = 0
        self.rear = -1
        self.front = -1
        self.queue = []
    def form_queue(self) -> list[T]:
        for i in range(0,self.size):
            self.queue.insert(i,-1)

        return self.queue
        
    
    def append_rear(self,item):
        if self.capcity < self.size:
            if self.front == -1 and self.rear == -1:
                self.front +=1
                self.rear +=1
                self.queue[self.rear] = item

            elif self.rear < self.size:
                self.rear += 1
                self.queue[self.rear] = item
            
    def roatate(self,rotate):
        print(self.front)
        if self.rear > -1 and rotate < self.capcity:
            i = -1
            while i!=rotate:
                temp = self.front
                self.front -= 1
                x = self.rear
                while temp != x:
                    self.queue[temp+1] = self.queue[temp]
                    temp+=1
            

    def pop_left(self):
        if self.capcity >= 0:

            if self.front == self.rear and self.capcity == 1:
                temp = self.queue[self.front]
                self.queue = []
                self.front,self.rear = -1
                return temp
            else:
                temp = self.queue[self.front]
                self.queue = self.queue[self.front+1:]
                self.front +=1
                self.capcity -=1
                return temp
        
        else:
            print('Queu is empty')
            return -1

"""
front[-------------]rear
"""

q = Queues[int](size = 10)
q.queue = [x for x in range(10)]
q.capcity = 10
q.front = 0
q.rear = 9
item = q.pop_left()
print('item',item)
print(q.queue)
print(q.capcity)
q.roatate(3)
print(q.queue)
