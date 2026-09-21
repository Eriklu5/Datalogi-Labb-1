class DictHash:
    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, data): #som lagrar data som value i din dictionary, med nyckel som key:
        self.dictionary[nyckel] = data

    def search(self, nyckel): #som slår upp nyckel i din dictionary och returnerar data:
        return self.dictionary.get(nyckel)
        
    def __getitem__(self, nyckel):
        self.search(self, nyckel)

    def __contains__(self, nyckel):
        if self.get(nyckel):
            return True
        else: return False
        # return finns() 

""" def create_hash_table(lista):
    lookup = {}

    for song in lista:
        lookup[song.title] = song

    return lookup

def hash_search(lookup, target):
    if lookup.get(target.title) != None:
        return lookup.get(target.title)
    else: print(False) """

    
class Hashtable:
    pass



class Drama: # drama klass
    def __init__(self,drama_info):
        self.drama_name = drama_info[0]
        self.rating = float(drama_info[1])
        self.actors = drama_info[2]
        self.viewship_rate = float(drama_info[3])
        self.genre = drama_info[4]
        self.director = drama_info[5]
        self.writer = drama_info[6]
        self.year = int(drama_info[7])
        self.no_of_episodes = int(drama_info[8])
        self.network = drama_info[9]

    def __str__(self):
        return(self.drama_name)

    def __lt__(self, other):
        return self.rating < other.rating
    
    def produced_by(self):
        return self.director, self.writer
    
    def years_after_1900(self):
        if self.year<1900:
            return None
        else:
            return self.year-1900


import csv

def read_file(filename): # läser in en fil och skriver ut dess innehåll
    with open(filename, mode="r") as file:
        csvfile = csv.reader(file,delimiter="\t")
        for line in csvfile:
            print(line)


def read_drama_from_file(dramafile): # läser in en fil och skapar en lista av drama objekt
    drama_list = list()
    with open(dramafile, mode="r") as file:
        csvfile = csv.reader(file,delimiter=",")
        next(csvfile)
        for line in csvfile:
            new_drama = Drama(line)
            DictHash.store(new_drama.drama_name, new_drama)
            drama_list.append(new_drama)
    return drama_list





print(DictHash.search("King the land"))


dict.__setitem__(self, key, value)
dict.__getitem__(self.table, "key")
dict.__contains__(self.table, "key")