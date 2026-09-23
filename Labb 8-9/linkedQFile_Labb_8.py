class Node:
    # Skapar en nod som innehåller ett värde och pekar på nästa nod, annars på none
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQ:
    """Skapar en länkad lista av noder 
    \n Metoder: 
    \n  def enqueue(any) lägger till element i kö
    \n  def dequeue(any) returerar element först i kö
    \n  def isEmpty() kollar om det finns ett första element, returerar True eller False """
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

    def peek(self):
        if self.__first.data == None:
            return False
        return self.__first.data
