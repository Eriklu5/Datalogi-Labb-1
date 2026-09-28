import timeit
timeit.timeit

import random


class song:
    def __init__(self, track_id, song_id, artist, title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __str__(self):
        return self.title + "av " + self.artist

    def __lt__(self, other):
        return self.artist < other.artist
    
    def __eq__(self,other):
        return self.artist == other.artist


def readfile(file = "unique_tracks.txt"):
    rader = []
    with open(file, "r") as file:
        for rad in file:
            rad = rad.split("<SEP>")
            rader.append(song(*rad))
    return rader


def linear_search(list, target):
    for x in list:
        if x == target:
            return True
    return False


def binary_search(list, target): # behöver en sorterad lista
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return list[mid]
        elif list[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return None


def create_hash_table(lista):
    lookup = {}

    for song in lista:
        lookup[song.title] = song

    return lookup

def hash_search(lookup, target):
    return lookup.get(target.title)


def insertion_sort(list): #o(n^2) (geeksforgeeks.org/dsa/insertion-sort-algorithm)
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1

        while j>=0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key


def quicksort(data): # Föreläsnings anteckningar
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v



def sökningstest(listor): # tar tid på olika sökalgoritmer. indata: en lista med olika långa listor i
    for lista in listor:
        print("n =",len(lista))

        linjtid = timeit.timeit(stmt = lambda: linear_search(lista, lista[random.randint(0,(len(lista)-1))]), number = 10000) # tar tid på linjärsökning
        print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

        lista.sort()

        bintid = timeit.timeit(stmt = lambda: binary_search(lista, lista[random.randint(0,(len(lista)-1))]), number = 10000) # tar tid på binär sökning 
        print("Binärsökningen tog", round(bintid, 4) , "sekunder")

        dictonary = create_hash_table(lista)
        hashtid = timeit.timeit(stmt = lambda: hash_search(dictonary, lista[random.randint(0,(len(lista)-1))]), number = 10000) # tar tid på sökning i en hash tabell
        print("Hashsökningen tog", round(hashtid, 4) , "sekunder")


def sorteringstest(listor): # tar tid på olika sökalgoritmer. indata: en lista med olika långa listor i
    for lista in listor:
        print("n =",len(lista))
        inserttid = timeit.timeit(stmt = lambda: insertion_sort(lista), number = 1) # tar tid på sortering med insertion sort
        print("Insertion sort tog ",round(inserttid,4), "sekunder")

        quicktid = timeit.timeit(stmt = lambda: quicksort(lista), number = 1) # tar tid på sortering med quicksort
        print("Quicksort tog ",round(quicktid,4), "sekunder")


def main():

    listan = readfile()
    listan2 = listan[0:] # måste ha två olika listor för sökningen och sorteringen. Annars kommer den vara sorterad när den ska vara osorterad vilket stör jämförelsen
    listor = [listan[0:250000], listan[0:500000], listan]
    sökningstest(listor)
    listor2 = [listan2[0:1000],listan2[0:10000],listan2[0:100000],listan2]
    sorteringstest(listor2)

main()


"""
Letade efter en slumpad artist.
Det finns flera låtar av samma artist i listan vilket 
jag tror tjänar linjärsökning mest eftersom det ökar chansen 
att hitta en låt av rätt artist tidigt i listan.
Det försämmrar antagligen quicksort och skulle kunna 
försämra sökning i hashtabbel men vår hashtabell skriver 
över dubbletter vilket gör att det inte bör bli några krockar


Tidskomplexitet sökning
Linjärsökning   Binärsökning    Sökning i hashtabell
O(1)-O(n)       O(log(n))       O(1) (i praktiken ofta lite sämre pga dubletter)

Uppmätta tider sökning (number = 10000) (Mätt i sekunder)
n =                     250000  500000  1000000
Linjärsökning           48.7021 73.9763 78.0395
Binärsökning            0.0835  0.0816  0.0906
Sökning i hashtabell    0.0138  0.0146  0.0172

Brett sätt stämmer beetendet med teorin
Linjärsökningen tog ett mycket mindre hopp i tid mellan n=500000 och n=1000000 än 
förväntat men detta beror nog på att samma artist finns med flera gånger i listan
så chansen att artisten finns längre fram i listan ökar. 
Jag tror att Linjärsökningen hade tur många gånger för n=1000000
eller att det finns många dubbletter i andra halvan av 1000000 listan.
Eftersom de mindre n bestod av de första 250000 respektive 500000 av 1000000 listan


Tidskomplexitet sortering
Insättningssortering    Quicksort
O(n^2)                  O(n*log(n))

Uppmätta tider sortering (number = 1) (Mätt i sekunder)
n =                     1000    10000   100000  1000000
Insättningssortering    0.0906  9.8751  1185.02 Körde inte, uppskattar att det skulle ta ≈30 h 
Quicksort               0.0024  0.0399  0.4841  6.7564

Följer vad man skulle förvänta sig från teorin
Insättningssorteringen ökar ganska tydligt med en faktor 
av ungefär 100 när mängden data ökar med faktor 10 (100=10^2) 
Quicksort ser ut att öka ungefär med lite mer än faktor 10
vilket skulle motsvara en tidskomplexitet på n istället för n*log(n).
Detta beror nog på att listan innehåller dubbletter vilket gör 
quicksort långsammare än ideal fallet eftersom det är svårare att 
effektiv dela upp mängder i större och mindre om det finns flera lika stora värden
"""