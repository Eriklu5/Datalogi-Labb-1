from bintreeFile import Bintree
from linkedQFile import LinkedQ

ALFABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]


gamla = Bintree()
svenska = Bintree()


class ParentNode:
    """ Nod, lagrar ett ord samt pekar på förälder nod """
    def __init__(self, ord, förälder = None):
        self.ord = ord
        self.förälder = förälder


class SolutionFound(Exception):
    pass


with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet


def makechildren(stamfar,q, slutord):
    """ In parametrar: noden stamfar och den linkade listan q 
        \n Retur värden: inga
        \n använder ordet lagrat i noden och skapar nya ord genom 
        enbokstavsändring utav nodens ord. Dessa stoppas in i kön om de finns i svenska sökträdet
        """
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
                if nyttord == slutord:
                    writechain(ParentNode(nyttord))

def writechain(slutordsnod):
    # "Ska skrivas rekursivt, så att man får ut kedjan med slutordet sist." Alltså Pre-order liknande???
    if slutordsnod == None:
        return
    writechain(slutordsnod.förälder)
    print(slutordsnod.ord)

 
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
        makechildren(nod, q, slutord) # Möjligtvis ska makechildren ta in slutord som parameter och sedan ska makechildren göra utskriften "det finns en väg". 
        # Eftersom i labb 5 beskrivningen står det att makechildren ska, om den hittat slutordet från nya orden, anropa writechain som ger utskrift

    else:
        print("Det finns ingen väg till", slutord)


main()