# Fortsättning av labb 8





from sys import stdin


def main():
    #stdin = open("indata1.txt") #Lätt att ändra för att testa indata från fil
    rad = stdin.readline()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:
            q.enqueue(tkn)
        try:
            readformel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            rest = str(q).strip()
            print(felet, "vid radslutet", rest)
        rad = stdin.readline()

main()