
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
"""
# detta är inte nödvändigt men att använda deom kanske gör koden mer lättläslig?
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
"""


class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self,item):
        if self.__first == None:
            self.__first = Node(item)
            self.__last = self.__first
        else: 
            self.__last.next = Node(item)
            self.__last = self.__last.next

    def dequeue(self):
        item = self.__first
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            self.__first = self.__first.next
        return item.data

    def isEmpty(self):
        return self.__first == None



import unittest

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

if __name__ == "__main__":
    unittest.main()