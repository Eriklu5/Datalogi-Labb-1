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


if __name__=="__main__":
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
