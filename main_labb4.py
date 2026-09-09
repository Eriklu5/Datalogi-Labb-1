from bintreeFile import Bintree
from linkedQFile import LinkedQ

ALFABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]



svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet




gamla = Bintree()




def makechildren(startord,q):
    for index, versal in enumerate(startord):
        for bokstav in ALFABET:
            nyttord = startord
            if bokstav == versal:
                pass
            
            else: 
                nyttord = nyttord[:index] + bokstav + nyttord[index + 1:]
                if nyttord in svenska and nyttord not in gamla:
                    q.enqueue(nyttord)
                    gamla.put(nyttord)



def main():

    q = LinkedQ()
    startord = input("Skriv startord: ")
    slutord = input("Skriv slutord: ")


    q.enqueue(startord)
    while not q.isEmpty():
        word = q.dequeue()
        makechildren(word, q)
        if word == slutord:
            print("Det finns en väg till", slutord)
            break

    if q.isEmpty():
        print("Det finns ingen väg till", slutord)


main()