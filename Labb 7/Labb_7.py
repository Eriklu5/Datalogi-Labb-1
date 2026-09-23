from hashtable import Hashtable
from Labb_1 import Drama
import csv



""" Gör om labb 7 fast utan en linjär probning, utan med en dubbel hashning eller en annan probning!. 
    Gör om labb 6 fast med en implementering av radix sort? """

class DictHash:
    def __init__(self):
        self.dictionary = {}

    # som lagrar data som value i din dictionary, med nyckel som key:
    def store(self, nyckel, data):
        # dict.__setitem__(self, nyckel, data)
        self.dictionary[nyckel] = data

    # som slår upp nyckel i din dictionary och returnerar data:
    def search(self, nyckel):
        return self.dictionary.get(nyckel, f"{nyckel} finns inte i listan")
        # Kan ändra till direktör genom t.ex. .director i slutet, denna printar ut __str__ vilket är .drama_name

    def __getitem__(self, nyckel):
        # dict.__getitem__(self.dictionary, "key")
        self.search(self, nyckel)

    def __contains__(self, nyckel):
        # dict.__contains__(self.dictionary, "key")
        if self.dictionary.get(nyckel):
            return True
        else:
            return False
        # return finns()


Hashtabell = DictHash()


# läser in en fil och skapar en lista av drama objekt
def read_drama_from_file(dramafile):
    with open(dramafile, mode="r") as file:
        csvfile = csv.reader(file, delimiter=",")
        next(csvfile)
        for line in csvfile:
            new_drama = Drama(line)
            Hashtabell.store(new_drama.drama_name, new_drama)


read_drama_from_file("kdrama.csv")
print(f"\n{Hashtabell.search("Vincenzo")}")
print(Hashtabell.search("Reply 1988"))
print(Hashtabell.search("Reborn Rich"))
print(Hashtabell.search("Mission Impossible"))


def main():
    hashtable = None

    while True:
        line = input()
        key, *value = line.split()
        if key == '#':
            print('#')
            break
        elif key == 'init' and len(value) > 0:
            size = int(value[0])
            hashtable = Hashtable(size)
            print('New size:', size)
        elif len(value) > 0:
            hashtable.store(key, value[0])
            print(key, '<-', value[0])
        else:
            try:
                value = hashtable.search(key)
                print(f'{key}: {value}')
            except KeyError:
                print('KeyError:', key)


if __name__ == "__main__":
    main()


""" 
Definiera en klass HashNode för hashtabellens noder. Noderna måste innehålla både nyckel och värde.
Definiera en klass Hashtable som representerar hashtabellen. Hashtable ska ha samma funktionalitet som DictHash.
Du måste skriva en egen hashfunktion, som ger en bra fördelning över hela tabellen.
Någon krockhantering måste ingå, t ex krocklistor eller probning.
Du ska använda KeyError för att tala om att en nyckel inte finns. 




förklara varför hashning ger snabb sökning,
    Linjär sökning i en oordnad lista av längd n tar i genomsnitt n/2 jämförelser, 
    binär sökning i en sorterad lista log(n) 
    men hashning går direkt på målet och kräver bara drygt en jämförelse. 
    Detta eftersom den kan utföra en snabb beräkning med hashfunktionen och sedan titta på just det elementet istället för att gå igenom ett intervall

skissa hashtabellen,

motivera ditt val av hashfunktion, krockhantering och tabellstorlek genom att
    redogöra för hur bra fördelningen är, t.ex. genom att mäta hur många krockar det är som mest vid insättning,

    beskriva och rita hur din krockhantering fungerar,
    
    """
