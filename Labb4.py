from bintreeFile import Bintree

alfabetet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
svenska = Bintree()
gamla = Bintree()

with open("Datalogi-Labb-1/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

startord = input("Vad är startordet?")
slutord = input("Vad är slutordet?")

def makechildern(ord):
    pass
