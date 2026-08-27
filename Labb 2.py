#labb 2
from array import array

class ArrayQ():
    def __init__(self):
        self.__items = array("b")

    def is_empty(self):
        return not self.__items

    def enqueue(self,item):
            self.__items.append(item)


    def dequeue(self):
        item = self.__items.pop(0)
        return item



""""
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
print(q.is_empty())
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
print(q.is_empty())
"""

def trolleri():
    kortlek = ArrayQ()
    kort_ordning_in = input("Vilken ordning ligger korten i?")
    kort_ordning = kort_ordning_in.split(" ")
    for kort in kort_ordning:
        kortlek.enqueue(int(kort))
    print("De kommer ut i denna ordning: ",end="")
    while not kortlek.is_empty():
        kort_i_hand = kortlek.dequeue()
        kortlek.enqueue(kort_i_hand)
        print(kortlek.dequeue(),end=" ")

trolleri()

#gjort till och med deluppgift 3