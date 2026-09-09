from bintreeFile import Bintree
from linkedQFile import LinkedQ

class ParentNode:
    """ Nod, lagrar ett ord samt pekar på förälder nod """
    def __init__(self, ord, förälder = None):
        self.ord = ord
        self.förälder = förälder


alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
svenska = Bintree()
gamla = Bintree()

with open("Datalogi-Labb-1/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

def makechildren(startord,kö):
    for index, versal in enumerate(startord.ord): 
        # funkar en gång med () men inte en andra utan () funkar den inte första gången
        for bokstav in alfabet:
            nyttord = startord.ord
            if bokstav == versal:
                pass
            else: 
                nyttord = nyttord[:index] + bokstav + nyttord[(1+index):]
                if nyttord in svenska and not nyttord in gamla:
                    kö.enqueue(ParentNode(nyttord,startord))
                    gamla.put(nyttord)



def writechain(node):
    if node.förälder != None:
        writechain(node.förälder)
    print(node.ord,end=" ")


q = LinkedQ()
startord = input("Vad är startordet? ").lower()
slutord = input("Vad är slutordet? ").lower()


q.enqueue(ParentNode(startord))

while not q.isEmpty():
    word = q.dequeue()
    makechildren(word, q)
    if word.ord == slutord:    
        print("Det finns en väg från", startord, "till", slutord)
        writechain(word)
        break
else:
    print("Det finns ingen väg till", slutord)