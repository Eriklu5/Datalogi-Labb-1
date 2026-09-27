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


def linear_search(list, target): # beter sig väldigt konstigt om listan inte är sorterad
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



def sökningstest(listor):
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


def sorteringstest(listor):
    for lista in listor:
        print("n =",len(lista))
        inserttid = timeit.timeit(stmt = lambda: insertion_sort(lista), number = 1) # tar tid på sökning i en hash tabell
        print("Insertion sort tog ",round(inserttid,4), "sekunder")

        quicktid = timeit.timeit(stmt = lambda: quicksort(lista), number = 1) # tar tid på sökning i en hash tabell
        print("Quicksort tog ",round(quicktid,4), "sekunder")


def main():

    listan = readfile()
    listan2 = listan[0:]
    listor = [listan[0:250000], listan[0:500000], listan]
    sökningstest(listor)
    listor2 = [listan2[0:1000],listan2[0:10000],listan2[0:100000],listan2]
    sorteringstest(listor2)

main()