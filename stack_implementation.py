#1 using list
stack1 = []

stack1.append("goblin")
stack1.append("soot")
stack1.append("goomba")

print(stack1)

print(stack1.pop())
print(stack1.pop())

print(stack1)

#2 using collections.deque
from collections import deque

stack2 = deque()

stack2.append("goblin")
stack2.append("soot")
stack2.append("goomba")

print(stack2)
print(stack2.pop())
print(stack2.pop())
print(stack2)

#3 using queue.LifoQueue
from queue import LifoQueue

stack3 = LifoQueue(maxsize=3)

print(stack3.qsize())

stack3.put("Anya")
stack3.put("Loid")
stack3.put("Yor")
print(stack3.full())

print(stack3.get())
print(stack3.get())
print(stack3.get())
print(stack3.empty())
