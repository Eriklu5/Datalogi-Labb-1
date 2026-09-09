from bintreeFile import Bintree
from linkedQFile import LinkedQ

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
    for index, versal in enumerate(startord):
        for bokstav in alfabet:
            nyttord = startord
            if bokstav == versal:
                pass
            else: 
                nyttord = nyttord[:index] + bokstav + nyttord[(1+index):]
                if nyttord in svenska and not nyttord in gamla:
                    kö.enqueue(nyttord)
                    gamla.put(nyttord)


q = LinkedQ()
startord = input("Vad är startordet? ")
slutord = input("Vad är slutordet? ")


q.enqueue(startord)
while not q.isEmpty():
    word = q.dequeue()
    makechildren(word, q)
    if word == slutord:    
        print("Det finns en väg till", slutord)
        
        break
else:
    print("Det finns ingen väg till", slutord)