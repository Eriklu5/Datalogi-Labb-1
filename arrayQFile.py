from array import array


class ArrayQ:

    def __init__(self):
        self.__data = array('b')


    def enqueue(self, data):
        self.__data.append(data)


    def dequeue(self):
        item = self.__data.pop(0)
        return item


    def isEmpty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False






if __name__ == "__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
