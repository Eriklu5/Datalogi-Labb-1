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


def makechildren(stamfar, q, slutord):
    """ In parametrar: noden stamfar och den linkade listan q 
        \n Retur värden: inga
        \n använder ordet lagrat i noden och skapar nya ord genom 
        enbokstavsändring utav nodens ord. Dessa stoppas in i kön om de finns i svenska sökträdet
        """
    for index, versal in enumerate(stamfar.ord):
        for bokstav in ALFABET:
            nyttord = stamfar.ord
            if bokstav == versal:
                pass
            else: 
                nyttord = nyttord[:index] + bokstav + nyttord[index + 1:]
                if nyttord == slutord: 
                    writechain(ParentNode(nyttord, stamfar))
                    raise SolutionFound            
                elif nyttord in svenska and not nyttord in gamla:
                    q.enqueue(ParentNode(nyttord, stamfar))
                    gamla.put(nyttord)

                    

def writechain(slutordsnod):
    # "Ska skrivas rekursivt, så att man får ut kedjan med slutordet sist." Alltså Pre-order liknande???
    if slutordsnod.förälder != None:  
        writechain(slutordsnod.förälder)
    print(slutordsnod.ord)

 
def main():

    q = LinkedQ()
    startord = input("Skriv startord: ").strip().lower()
    slutord = input("Skriv slutord: ").strip().lower()
    
    stamfar = ParentNode(startord)
    q.enqueue(stamfar)
    gamla.put(startord)

    try:
        while not q.isEmpty():
            nod = q.dequeue()
            if nod.ord == slutord:
                print("Det finns en väg till", slutord)
                break
            makechildren(nod, q, slutord) # Möjligtvis ska makechildren ta in slutord som parameter och sedan ska makechildren göra utskriften "det finns en väg". 
            # Eftersom i labb 5 beskrivningen står det att makechildren ska, om den hittat slutordet från nya orden, anropa writechain som ger utskrift

        else:
            print("Det finns ingen väg till", slutord)
    except SolutionFound: print("Det finns en väg till", slutord)

main()