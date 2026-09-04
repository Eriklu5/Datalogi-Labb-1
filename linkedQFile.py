        
class Node:
    # Skapar en nod som innehåller ett värde och pekar på nästa nod, annars på none
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQ:
    # Skapar en linkad lista av noder med metoder som lägger till, tar bort, och kollar om listan är tom
    def __init__(self):
        self.__first = None
        self.__last = None


    def enqueue(self, data):
        # Lägger till, två fall, första om listan är tom annars om den inte är det
        if self.__first == None:
            self.__first = Node(data)
            self.__last = self.__first
        else:
            self.__last.next = Node(data)
            self.__last = self.__last.next

    def dequeue(self):
        # Tar bort första noden och returnar dess värde, om den är tom så returnar None istället
        first = self.__first

        if self.isEmpty(): 
            return None
        
        elif self.__first == self.__last:
            self.__first = None
            self.__last = None

        else: 
            self.__first = self.__first.next

        return first.data

    def isEmpty(self):
        # Kollar om det finns ett första element, om inte är den tom
        if self.__first == None:
            return True
        else:
            return False




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