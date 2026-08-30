from array import array

class ArrayQ():
    def __init__(self): 
        self.__items = array("b") # en array som tar heltal

    def isEmpty(self): # Kollar om kön är tom ocg rturnerar True eller False
        return not self.__items

    def enqueue(self,item): # Lägger ett heltal sist i kön
            self.__items.append(item)

    def dequeue(self): # Plockar ut och returnerar talet sokm ligger först i kön
        item = self.__items.pop(0)
        return item

if __name__=="__main__": # Test för att se att klassen fungerar korrekt
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
    print(q.isEmpty())
