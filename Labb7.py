import csv


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
        


def read_drama_from_file(dramafile): # läser in en fil och skapar en dictonary av drama objekt
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

drama_dict = read_drama_from_file("Tillämpad Datalogi/Labb 1/kdrama.csv")
print(drama_dict.search("Legend of the Blue Sea"))
print(drama_dict.search("Epic Town"))


class HashNode:
    """Noder till klassen Hashtable """
    def __init__(self, key = "", data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data

# Från boken och canvas:
class Hashtable:
    
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.slots = [None] *size
        # om man vill hantera krockar med buckets (arrays i hashindex), [[] for _ in range(size)] https://www.w3schools.com/dsa/dsa_data_hashsets.php



    def store(self, key, data):
        """key är nyckeln
            data är objektet som ska lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        hash_value = self.hashfunction(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = HashNode(key, data)
            

        else:
            if self.slots[hash_value].key == key:
                self.slots[hash_value] = HashNode(key, data)  # ersätt
            else:
                next_slot = self.rehash(hash_value)
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot].key != key # Noden är fylld, och key är olika
                ):
                    next_slot = self.rehash(next_slot) # Dvs den fortsätter att itererara genom nya noder tills den hittar antingen (se nedan)

                if self.slots[next_slot] is None: # Noden är inte fylld:
                    self.slots[next_slot] = HashNode(key, data)
                else: # Noden är fylld, key är samma, while loopen itererar för nod fylld och key är olika 
                    # dvs koden når endast hit om det while-loopen inte stämmer och noden inte är fylld (ty ovan if-sats).
                    self.slots[next_slot].data = data

                    
    def search(self, key):
        """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
        start_slot = self.hashfunction(key) # Kollar vilken position som nyckeln borde befinna sig

        position = start_slot
        while self.slots[position] is not None: # Kollar så att elementet är fyllt
            if self.slots[position].key == key: # Är sparade elementet samma som vi söker?
                return self.slots[position].data # Returnera det isåfall
            else:
                position = self.rehash(position) # Följ efter de eventuella stegen som skulle tagits för noden om den lagrats men dess hashvärde var redan taget. Dvs leta efter fri position
                if position == start_slot: # Om vi kommer fram till ett None element så bryts while-loopen och vi får error, men om vi kommer tillbaka till start elementet måste vi manuellt bryta loopen
                    self.slots[position] = None
            
        else: raise KeyError

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, data):
        self.store(key, data)

    def hashfunction(self, key):
        """key är nyckeln
         Beräknar hashfunktionen för key"""
        h = 0 
        for tkn in key: # Tagen från föreläsning 10, den med bäst fördelning 
            h = 32*h  + ord(tkn)
        return h % self.size


    def rehash(self, old_hash): # Finns olika metoder för att hitta en ny plats i hashtabellen när en krock sker. Detta är "linjär probning", 
        # dvs leta efter ledig plats med inkrement 1 (en hashtabell ska ha många fler platser än vad som förväntas lagras) detta ger dock problemet "klustring" 
        # då vi får en väldigt stor densitet av lagrade element i listan där det redan skett en krock. 
        # Finns andra typer av probning (Open addressing) kvadratisk probning (inkrement kvadratiskt), dubbelhashning (också en probning, använd en separat hashing och multiplicera med det inkrementet) 
        # (Seperate chaining) buckets (då ett hashvärde har en lista (array) i sig med flera lediga positioner)
        return (old_hash + 1) % self.size