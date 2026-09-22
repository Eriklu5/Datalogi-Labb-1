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


from hashtable import Hashtable

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
        self.slots = [None] *size


    def store(self, key, data):
        """key är nyckeln
            data är objektet som ska lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        hash_value = self.hashfunction(key, len(self.slots))

        if self.slots[hash_value] is None:
            node = HashNode(key, data)
            self.slots[hash_value] = node

        else:
            if self.slots[hash_value].key == key:
                self.slots[hash_value] = HashNode(key, data)  # ersätt
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (
                    self.slots[next_slot] is not None
                    and self.slots[next_slot].key != key # Noden är fylld, och key är olika
                ):
                    next_slot = self.rehash(next_slot, len(self.slots)) # Dvs den fortsätter att itererara genom nya noder tills den hittar antingen (se nedan)

                if self.slots[next_slot] is None: # Noden är inte fylld:
                    self.slots[next_slot] = HashNode(key, data)
                else: # Noden är fylld, key är samma, while loopen itererar för nod fylld och key är olika 
                    # dvs koden når endast hit om det while-loopen inte stämmer och noden inte är fylld (ty ovan if-sats).
                    self.slots[next_slot].data = data

                    
    def search(self, key):
        """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
        start_slot = self.hash_function(key, len(self.slots)) # Kollar vilken position som nyckeln borde befinna sig

        position = start_slot
        while self.slots[position] is not None: # Kollar om elementet är fyllt
            if self.slots[position] == key: # Är sparade elementet samma som vi söker?
                return self.data[position] # Returnera det isåfall
            else:
                position = self.rehash(position, len(self.slots)) # Följ efter de eventuella stegen som skulle tagits för noden om den lagrats men dess hashvärde var redan taget. Dvs leta efter fri position
                if position == start_slot: # Om vi kommer fram till ett None element så bryts while-loopen och vi får error, men om vi kommer tillbaka till start elementet måste vi manuellt bryta loopen
                    return None
            
        else: raise KeyError

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, data):
        self.store(key, data)

    def hashfunction(self, key):
      """key är nyckeln
         Beräknar hashfunktionen för key"""
      return key % self.size


    def rehash(self, old_hash, size): # Finns olika metoder för att hitta en ny plats i hashtabellen när en krock sker. Tror detta är probning, 
        # dvs leta efter ledig plats (en hashtabell ska ha många fler platser än vad som förväntas lagras). 
        # Finns annars krocklistor, då ett hashvärde har en lista i sig med flera lediga positioner
        return (old_hash + 1) % size


def main():
    try:

        pass

    except: KeyError 
# Detta har redan skrivits, kommer snart att läggas till...

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