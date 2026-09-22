from Labb_1 import Drama
import csv


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

class Hashtable:
    def __init__(self, size):
        self.size = size
        ...

    def store(self, key, data):
        ...

    def search(self, key):
        """Hämtar det objekt som finns lagrat med
        nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception,
        KeyError."""
        ...
       # else:
        #    raise KeyError

    def hashfunction(self, key):
        pass


""" Hashtabellen ska åtminstone ha följande operationer:

store(key, data) Lägg in data med nyckeln key i hashtabellen. 
data = search(key) Hämta data som hör till key. 
f = hashfunction(key) Beräkna hashfunktionen för key """

""" def create_hash_table(lista):
    lookup = {}

    for song in lista:
        lookup[song.title] = song

    return lookup

def hash_search(lookup, target):
    if lookup.get(target.title) != None:
        return lookup.get(target.title)
    else: print(False) """
