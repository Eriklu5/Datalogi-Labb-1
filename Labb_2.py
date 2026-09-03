# Labb 2. pverison
from array import array
from collections import deque



numbers = deque([3,4,5,6,7])
numbers.append(4)
numbers.appendleft(32)


class ArrayQ():
    def __innit__(self):
        self.__array=array


    def enqueue(self, value):
        value = None 
    def dequeue(self):
        None
    def isEmpty():
        if len(array) == 0:
            return True
        else:
            return False

        
class Node:
    def __innit__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __innit__(self):
        self.head=None


first = Node(10)
first.next = Node(20)
first.next = Node(30)


# Test
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")




""" 
Q = array('b')

Q.append(int("3" + "4"))

Q.insert(0, 2)

Q.pop(0)
print(Q)

 """