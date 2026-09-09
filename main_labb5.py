from bintreeFile import Bintree
from linkedQFile import LinkedQ

ALFABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]


gamla = Bintree()
svenska = Bintree()


class ParentNode:
    def __init__(self, ord, förälder = None):
        self.ord = ord
        self.förälder = förälder


with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet


def makechildren(stamfar,q):
    startord = stamfar.ord
    for index, versal in enumerate(startord):
        for bokstav in ALFABET:
            nyttord = startord
            if bokstav == versal:
                pass
            else: 
                nyttord = nyttord[:index] + bokstav + nyttord[index + 1:]
                if nyttord in svenska and nyttord not in gamla:
                    gamla.put(nyttord)
                    nod = ParentNode(nyttord, stamfar)
                    q.enqueue(nod)

def writechain(slutordsnod):
    pass

def main():

    q = LinkedQ()
    startord = input("Skriv startord: ")
    slutord = input("Skriv slutord: ")

    stamfar = ParentNode(startord)

    q.enqueue(stamfar)
    while not q.isEmpty():
        nod = q.dequeue()
        if nod.ord == slutord:
            print("Det finns en väg till", slutord)
            break
        makechildren(nod, q)

    else:
        print("Det finns ingen väg till", slutord)


main()