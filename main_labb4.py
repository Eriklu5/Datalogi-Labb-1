from bintreeFile import Bintree


svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

gamla = Bintree()


alfabet = ["a", "b"]


def makechildren(startord):
    for index, versal in enumerate(startord):
        for bokstav in alfabet:
            nyttord = startord
            if bokstav == versal:
                pass
            else: 
                nyttord[index] = bokstav
                if nyttord in svenska() and not nyttord in gamla():
                    print(nyttord)
                    gamla.put(nyttord)

                #if nyttord (in svenska() and not in gamla())







startord = input()
slutord = input()

makechildren(startord)