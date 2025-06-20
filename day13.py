#Today I learned about first of Queue Data Structure, however I already know its working but didn't know how to implement it in python, whereas now I understand it can be implemented using list where it have methods like insert and pop and alternative option to implement queue data structure is deque module from collections. Deque modules have appendleft methods to append. Along with that I saw a real case scenario where Queue data structure  is used, that is in Stock Market to update stock value in squence, then in seat allocation in college, etc.

#Today second thing which I learned is about Stack data structure, similarly like queue only I already know how it works but didn't know how to implement in python. Understand that with double ended queue, we can implement both stack and queue. Another imp thing which I learnt that list is not a good option to implement both data structure as it copies the element into another location in stack whenever initially implemented list gets full whereas not such problem arise with dqueue.

#Simplest Way implement queue and stack
queue = []
queue.insert(0,'darshil')
queue.insert(0,'jenil')
queue.insert(0,'vedant')
print(queue)
print(queue.pop())
print(queue)

stack = []
stack.append('darshil')
stack.append('jenil')
stack.append('vedant')
print(stack)
print(stack.pop())
print(stack)


#deque is a double ended queue, it can be use as a queue and stack as well. 
from collections import deque
class Queue:
    def __init__(self) -> None:
        self.buffer = deque()
    def enqueue(self,value):
        self.buffer.appendleft(value)
    def dequeue(self):
        return self.buffer.pop() #by default pop() pop out the value from the end of the list only or from right side
    def show_queue(self):
        print(self.buffer)

queue2 = Queue()
queue2.enqueue({'fruit name':'apple',
                'price':20,
                'quantity':50})
queue2.enqueue({'fruit name':'mango',
                'price':30,
                'quantity':80})
queue2.enqueue({'fruit name':'banana',
                'price':10,
                'quantity':60})
queue2.show_queue()
print(queue2.dequeue())
queue2.show_queue()


class Stack:
    def __init__(self) -> None:
        self.buffer = deque()
    def push(self,value):
        self.buffer.append(value)
    def pop(self):
        return self.buffer.pop()
    def show_stack(self):
        print(self.buffer)
    
stack2 = Stack()
stack2.push(30)
stack2.push(40)
stack2.push(50)
stack2.show_stack()
print(stack2.pop())
stack2.show_stack