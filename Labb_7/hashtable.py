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