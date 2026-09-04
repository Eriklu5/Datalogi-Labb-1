class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item


class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


        
def putta(p, newvalue):
    # Funktion som gör själva jobbet att stoppa in en ny nod
    if p == None:
        return Node(newvalue)

    elif newvalue < p.item:
        p.left = putta(p.left, newvalue)

    else:
        p.right = putta(p.right, newvalue)
        


def finns(p,value):
        # Funktion som gör själva jobbet att söka efter ett värde
    letar = True
    while letar:
        if p == None: 
            return False
        if value == p.item: 
            return True
        if value < p.item: 
            p = p.left
        if value > p.item: 
            p = p.right

def skriv(p):
    # Funktion som gör själva jobbet att skriva ut trädet
    if p != None:
        skriv(p.left)
        print(p.item)
        skriv(p.right)   



""" 
if "gurka" in svenska:           # Kolla om "gurka" finns i trädet
            - - -                        # (Operatorn in anropar metoden __contains__ 
                                            # som du ska implementera i din Bintree-klass)
            
svenska.write()                  # Skriver alla trädobjektets ord i bokstavsordning
 """