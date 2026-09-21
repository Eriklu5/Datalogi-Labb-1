def binary_search(list, target): # behöver en sorterad lista
    left, right = 0, len(list) - 1


    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return False


class song:
    def __init__(self, track_id, song_id, artist, title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __str__(self):
        return self.title + "av" + self.artist

    def __lt__(self, other):
        return self.artist < other.artist
    
    def __eq__(self,other):
        return self.artist == other.artist

def readfile(file = "Datalogi-Labb-1/unique_tracks.txt"):
    rader = []
    with open(file, "r") as file:
        for rad in file:
            rad = rad.split("<SEP>")
            rader.append(song(*rad))
    return rader



import timeit

timeit.timeit



def linear_search(list, target): # beter sig väldigt konstigt om listan inte är sorterad
    for x in list:
        if x == target:
            return True
    return False



def create_hash_table(lista):
    lookup = {}

    for song in lista:
        lookup[song.title] = song

    return lookup

def hash_search(lookup, target):
    return lookup.get(target.title)


def linjär_sök_test(lista):
    n = len(lista)
    #print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista

    linjtid = timeit.timeit(stmt = lambda: linear_search(lista, testartist), number = 100)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")



def binär_sök_test(lista):
    n = len(lista)
    #print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista

    linjtid = timeit.timeit(stmt = lambda: binary_search(lista, testartist), number = 100)
    print("binärsökningen tog", round(linjtid, 4) , "sekunder")


def hash_sök_test(lista):
    n = len(lista)
    #print("Antal element =", n)
    dictonary = create_hash_table(lista)
    sista = lista[n-1]
    testartist = sista

    linjtid = timeit.timeit(stmt = lambda: hash_search(dictonary, testartist), number = 100)
    print("Hashsökningen tog", round(linjtid, 4) , "sekunder")


listan = readfile()
mindreListan = listan[0:250000]
mellanListan = listan[0:500000]
listor = [mindreListan, mellanListan, listan]

for lista in listor:
    print("n =",len(lista))
    lista.sort()
    linjär_sök_test(lista)
    binär_sök_test(lista)
    hash_sök_test(lista)
