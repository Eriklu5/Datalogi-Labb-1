
class Node: # En nod som används i en länkad lista
    def __init__(self,initdata): # En nod innehåller två värden
        self.data = initdata # Ett värde
        self.next = None # Och vilken nästa nod i listan är


class LinkedQ: # En länkad lista/kö
    def __init__(self): # Listan innehåller värden för vilken nod som är först och sist i kön
        self.__first = None
        self.__last = None

    def enqueue(self,item): # Lägger data i en nod och lägger noden sist i kön
        if self.__first == None: # Om listan är tom
            self.__first = Node(item)
            self.__last = self.__first
        else: # Om listan redan innehåller noder
            self.__last.next = Node(item) 
            self.__last = self.__last.next

    def dequeue(self): # Tar ut den nod som är först i kön och returnerar dess data
        item = self.__first
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else: # Ändrar så att noden efter den första nu är den första
            self.__first = self.__first.next
        return item.data

    def isEmpty(self): # Kollar om kön är tom och returnerar True/False
        return self.__first == None



# Test för att se att klasserna fungerar korrekt
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