""" 
def binary_search(a_list, TrgVal):
    left, right = 0, len(a_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if a_list[mid] == TrgVal:
            print(TrgVal)
            return
        elif a_list[mid] < TrgVal:
            left = mid + 1
        else:
            right = mid - 1

    print(None)
    # https://leetcode.com/explore/learn/card/binary-search/125/template-i/938/


list = input().strip().split()


value = input().strip()
while value != "#": 
    binary_search(list, value)
    value = input()
 """



class song:
    def __init__(self, track_id, song_id, artist, title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.title = title

    def __str__(self):
        return self.title + "av " + self.artist


    def __lt__(self, other):
        return self.title < other.title



def readfile(file = "unique_tracks.txt"):
    rader = []
    with open(file, "r") as file:
        for rad in file:
            rad = rad.split("<SEP>")
            rader.append(song(*rad))
    return rader

""" 
Vad representerar parametern stmt?
    a statement to be timed

Vad representerar parametern number?
    number of executions.

Vad är det timeit tar tid på?
    Executes the setup statement once,
    and then returns the time it takes to execute the main statement a number of times. 

Vad skrivs ut av ett anrop av timeit?
    The default timer returns seconds as a float. 
    The argument is the number of times through the loop, defaulting to one million. """


import timeit

timeit.timeit



def linear_search(list, target):
    for x in list:
        if x == target:
            return x
    else:
        print(False)



def binary_search(list, target):
    left, right = 0, len(list) - 1


    while left <= right:
        mid = (left + right) // 2
        if list[mid].title == target.title:
            return target
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else: print(False)



""" def hash_search(list, target):
"""     """ GPT-5.6 Luna, Prompt: 
        def hash_search(list, target):
            dict() 
            """ """
    lookup = {}
    
    for i, value in enumerate(list):
        lookup[value] = i

    if lookup.get(target) != None:
        return lookup[target]
    else: print(False) """


def create_hash_table(lista):
    lookup = {}

    for song in lista:
        lookup[song.title] = song

    return lookup

def hash_search(lookup, target):
    if lookup.get(target.title) != None:
        return lookup.get(target.title)
    else: print(False)



search_function_list = [linear_search, binary_search]

def main():

    lista = readfile()
    dictionary = create_hash_table(lista)
    lista.sort()

    n = len(lista)
    print("Antal element =", n)
    
    sista = lista[n-1]
    testartist = sista

    for search_function in search_function_list:
        linjtid = timeit.timeit(stmt = lambda: search_function(lista, testartist), number = 100)
        print(search_function.__name__, "tog", round(linjtid, 4) , "sekunder\n")

    linjtid = timeit.timeit(stmt = lambda: hash_search(dictionary, testartist), number = 1000)
    print(hash_search.__name__, "tog", round(linjtid, 4) , "sekunder\n")
      
main()




def insertion_sort(list, n):
    for i in range(n):
        key = list[i]
        j = i - 1

        while j>=0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key


lista = [5, 2, 8, 1, 3]

insertion_sort(lista, len(lista))

print(lista)




""" Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain. 
Wikipedia"""



""" void insertionSort(int a[], int n) {
    // We treat a[0..i-1] as the sorted part, and a[i..end] as unsorted.
    for (int i = 1; i < n; i++) {
        int key = a[i];  // The value we want to insert into the sorted prefix.
        int j = i - 1;

        // Shift larger elements one position to the right
        // until we find where 'key' belongs.
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        // Place 'key' into the gap created by shifting.
        a[j + 1] = key;
    }
} """




def quick_sort():


    """ # https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/
# partition function
def partition(arr, low, high):
    
    # choose the pivot    for  in :
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1

# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# the QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr, 0, n - 1)
    
    for val in arr:
        print(val, end=" ")
     """



""" 
 # https://www.w3schools.com/dsa/dsa_algo_quicksort.php
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1 """


def partition(array, low, high):
    mid = (low + high) // 2
    array[mid], array[high] = array[high], array[mid]

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

""" 
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)

        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)
 """
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)



def main():

    lista = readfile("unique_eighth.txt")
    lista = lista[0:10000]
    n = len(lista)
    print("Antal element =", n)

    linjtid = timeit.timeit(stmt = lambda: insertion_sort(lista, n), number = 1)
    print(insertion_sort.__name__, "tog", round(linjtid, 4) , "sekunder\n")
      
main() 

def main():


    lista = readfile("unique_eighth.txt")
    lista = lista[0:10000]

    quicksort(lista)
    n = len(lista)
    print("Antal element =", n)

    linjtid = timeit.timeit(stmt = lambda: quicksort(lista), number = 1)
    print(quicksort.__name__, "tog", round(linjtid, 4) , "sekunder")
      
main() 




""" Förklara skillnaden i uppmätta tider när storleken på listan varieras:

mellan de olika sökningsmetoderna
mellan de olika sorteringsmetoderna. 



Visa hur dina sök-, och sorteringsfunktioner fungerar,
Förklara och redovisa vilken tidskomplexitet dina algoritmer har,
Förklara skillnaden i tid mellan de olika sökningsmetoderna och mellan de olika sorteringsmetoderna."""



























































from codecarbon import OfflineEmissionsTracker



tracker = OfflineEmissionsTracker(
    project_name = "helloworld",
    country_iso_code="SWE",         # välj Sverige som land för beräkning av koldioxidkonsumption
    log_level="error",              # kör spåraren i "tyst" läge
    save_to_file=False              # spara inte resultatet som csv-fil
)

tracker.start_task()
pass                                # spåraren tittar bara på det som händer mellan start_task och stop_task!
co2 = tracker.stop_task()           # lagra resultatet i en variabel

tracker.start_task()                # det går bra att spåra flera olika algoritmer i samma körning
pass
co2_b = tracker.stop_task()         # ...men kom ihåg att ändra variabelnamnet

print(co2.emissions * 1000)         # multiplicera med 1000 för att skriva ut i g CO2 (istället för kg)

""" 
Fyll i tider och koldioxidutsläpp i en tabell på samma sätt som du gjorde i uppgiften ovan. 

Modulen codecarbon utgår ifrån den genomsnittliga koldioxidproduktionen per kWh för det angivna landets elproduktion. Sverige har en relativt koldioxidsnål elproduktion; testa att ändra land till t ex USA eller Kina (CHN), där många molntjänsters servrar finns, och jämför resultaten!

 """