#1 using list (dequeue is slow, takes O(n). other methods take O(1))

q1 = []
q1.append("Mario") # Enqueue: add "Mario" to the end of the queue
q1.append("Peach") # Enqueue: add "Peach" to the end of the queue
q1.append("Bowser") # Enqueue: add "Bowser" to the end of the queue
print(q1)           # print out the queue with 3 elements: "Mario" "Peach" "Bowser"
print(q1.pop(0))    # Dequeue: delete "Mario" from the beginning of the queue
print(q1.pop(0))    # Dequeue: delete "Peach" from the beginning of the queue
print(q1.pop(0))    # Dequeue: delete "Bowser" from the beginning of the queue
print(q1)           # prints out the new queue with all elements deleted

#2 using collections.deque
from collections import deque   # from collections module, import deque class

q2 = deque()    # initialize an object under the deque class

q2.append("goblin")     # Enqueue
q2.append("soot")       # Enqueue
q2.append("goomba")     # Enqueue
print(q2)

print(q2.popleft())     # Dequeue: delete "goblin" from the beginning of the queue, and print out "goblin"
print(q2.popleft())     # Dequeue
print(q2)

#3 using queue.Queue
from queue import Queue    # from queue module, import Queue class

q3 = Queue(maxsize = 3)    # initialize an object under the Queue class with a max size of 3 slots

print(q3.qsize())          # print out the current size of the queue (0, because we haven't added in elements yet)

q3.put("aaa")              # Enqueue: put element "aaa" into the queue
q3.put("bbb")              # Enqueue
q3.put("ccc")              # Enqueue
print(q3.full())           # returns "True" if queue is full, "False" if not full

print(q3.get())            # Dequeue: delete "aaa" from the beginning of the queue, and print out "aaa"
print(q3.get())            # Dequeue
print(q3.get())            # Dequeue
print(q3.empty())          # returns "True: if queue is empty, "False" if not empty

q3.put(111)                # despite being emptied earlier, the max size of the queue remains 3
print(q3.empty())
print(q3.full())


