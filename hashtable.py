class HashNode:
    """Noder till klassen Hashtable """
    def __init__(self, key = "", data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data
      self.next = None

# Från boken och canvas:
class Hashtable:
    
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size # helst primtal
        self.slots = [None] *size


    def store(self, key, data):
        """key är nyckeln
            data är objektet som ska lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        
        hash_value = self.hashfunction(key)
        start_value = hash_value
        if self.slots[hash_value] is None:
            self.slots[hash_value] = HashNode(key, data)
            return
        i = 1
        while self.slots[hash_value] != None:
            if self.slots[hash_value].key == key: # Skriver över om samma key redan finns 
                self.slots[hash_value] = HashNode(key, data)
                return
            hash_value = start_value + i**2 # kavdratisk probning h+1.h+4,h+9 osv
            if hash_value >= self.size:
                hash_value = hash_value % self.size
            i += 1
        self.slots[hash_value] = HashNode(key, data)
        return

                    
    def search(self, key):
        """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
        
        hash_value = self.hashfunction(key)
        start_value = hash_value
        i = 1
        while self.slots[hash_value] != None: # Går samma väg som store gör vid krock
            if self.slots[hash_value].key == key:
                return self.slots[hash_value].data
            hash_value = start_value + i**2
            if hash_value >= self.size:
                hash_value = hash_value % self.size
            i += 1
        raise KeyError(key)

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, data):
        self.store(key, data)

    def hashfunction(self, key): # Beräknar hashfunktionen för key
        h = 0 
        for tkn in key: # Tagen från föreläsning 10, den med bäst fördelning 
            h = 32*h  + ord(tkn)
        return h % self.size
        
test = Hashtable(10)

test.store("bb","a")
test.store("ac","b")
test.store("ca","c")
test.store("bd","a")
test.store("fc","b")
test.store("cag","c")
test.store("ar","b")
test.store("caf","c")