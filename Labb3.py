from bintreeFile import Bintree


svenska = Bintree()
with open("Datalogi-Labb-1/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("Datalogi-Labb-1/engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for rad in engelskfil:
        orden = rad.strip(" ,!").split(" ")
        for ord in orden: 
            if not ord in engelska:
                engelska.put(ord)
                if ord in svenska:
                    print(ord, end = " ")