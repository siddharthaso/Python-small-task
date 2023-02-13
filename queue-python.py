""" Methods available inside Queue and LifoQueue class

Following are the important methods available inside Queue and LifoQueue class:

    put(item): This will put the item inside the queue.
    get(): This will return you an item from the queue.
    empty(): It will return true if the queue is empty and false if items are present.
    qsize(): returns the size of the queue.
    full(): returns true if the queue is full, otherwise false. """

# A queue is a container that holds data. There are two types of Queue, FIFO, and LIFO. 
# To work with FIFO queue , call the Queue class using the queue module imported as shown below:	

from queue import Queue
q1 = Queue()
q1.put(10)
q1.put('df')
print(q1.qsize())       #2
print(q1.get())         #10
print(q1.qsize())       #1

q2 = Queue(2)
print(q2.empty())        #True
q2.put(10)
q2.put(34)
print(q2.full())        #True
print(q2.get())         #10
print(q2.full())        #False

print("-----------------------------------------------------------------------------")

# To work with LIFO queue call the LifoQueue() class as shown below:	
from queue import LifoQueue
q1 = LifoQueue()
q1.put(10)
q1.put('df')
print(q1.qsize())       #2
print(q1.get())         #10
print(q1.qsize())       #1

q2 = LifoQueue(2)
print(q2.empty())        #True
q2.put(10)
q2.put(34)
print(q2.full())        #True
print(q2.get())         #34
print(q2.full())        #False


""" 
# Queue, LifoQueue, or PriorityQueue-------------------------------------------------
Queue.qsize()
Queue.empty()
Queue.full()
Queue.put(item, block=True, timeout=None)
Queue.put_nowait(item)
Queue.get(block=True, timeout=None)
Queue.get_nowait()
Queue.task_done()
Queue.join()

# SimpleQueue objects provide the public methods described below.
SimpleQueue.qsize()
SimpleQueue.empty()
SimpleQueue.put(item, block=True, timeout=None)
SimpleQueue.put_nowait(item)
SimpleQueue.get(block=True, timeout=None)
SimpleQueue.get_nowait() """


# The multiprocessing.Queue class is used to implement queued items for processed in parallel by multicurrent workers. 
# The multiprocessing.Queue shares data between processes and can store any pickle-able object. 
from multiprocessing import Queue  
que = Queue()  
que.put('Apple')  
que.put('Mango')  
que.put('Banana')  
print(que)          #<multiprocessing.queues.Queue object at 0x7f03c91f7280>
print(que.get())  #Apple
print(que.get())  #Mango
print(que.get())  #Banana


# This priority queue implements uses heapq internally and shares the same time and space complexities.
# The difference is the priority queue is coordinated and delivers locking semantics to backing multiple concurrent events and consumers.
from queue import PriorityQueue  
q = PriorityQueue()  
q.put((2, 'Apple'))  
q.put((1, 'Banana'))  
q.put((3, 'Mango'))  
while not q.empty():  
    next_item = q.get()  
    print(next_item)  