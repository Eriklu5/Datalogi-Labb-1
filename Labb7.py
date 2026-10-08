import csv
from hashtable import Hashtable

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
        


def read_drama_from_file1(dramafile): # läser in en fil och skapar en dictonary av drama objekt
    drama_dict = DictHash()
    with open(dramafile, mode="r") as file:
        csvfile = csv.reader(file,delimiter=",")
        next(csvfile)
        for line in csvfile:
            new_drama = Drama(line)
            drama_dict.store(new_drama.drama_name,new_drama)
    return drama_dict




class DictHash:
    def __init__(self):
        self.dictionary = {}

    # som lagrar data som value i din dictionary, med nyckel som key:
    def store(self, nyckel, data):
        # dict.__setitem__(self, nyckel, data)
        self.dictionary[nyckel] = data

    # som slår upp nyckel i din dictionary och returnerar data:
    def search(self, nyckel):
        return self.dictionary.get(nyckel,nyckel+" finns inte i listan")
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

drama_dict = read_drama_from_file1("Tillämpad Datalogi/Labb 1/kdrama.csv")
print(drama_dict.search("Legend of the Blue Sea"))
print(drama_dict.search("Epic Town"))



def get_closest_prime(number): # ger första större primtalet
    while True: # Tänkte att man kunde anrunda storleken med heltal men det är nog inte tillåtet
        for i in range(2,number+1):
            if i == number:
                return number
            if number % i == 0:
                break

        number += 1


def read_drama_from_file2(dramafile): # läser in en fil och skapar en hashtabel av drama objekt
    drama_list = []
    with open(dramafile, mode="r") as file:
        csvfile = csv.reader(file,delimiter=",")
        next(csvfile)
        for line in csvfile:
            new_drama = Drama(line)
            drama_list.append(new_drama)
    drama_hashtabell = Hashtable(get_closest_prime(len(drama_list)*2))
    for drama in drama_list:
        drama_hashtabell.store(drama.drama_name,drama)
    return drama_hashtabell

drama_hashtabell = read_drama_from_file2("Tillämpad Datalogi/Labb 1/kdrama.csv")

print(drama_hashtabell.search("Legend of the Blue Sea"))
print(drama_hashtabell.search("Epic Town"))
