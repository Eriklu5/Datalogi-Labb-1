
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
    if p == None: 
        return Node(newvalue)
    
    elif p.item > newvalue: # om värdet är samma så läggs det till höger borde kanske ha ett specialfall?
        p.left = putta(p.left,newvalue)
        return p
    else:
        p.right = putta(p.right,newvalue)
        return p

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
        elif value > p.item: 
            p = p.right


def skriv(p):
    # Funktion som gör själva jobbet att skriva ut trädet
    if p != None:
        skriv(p.left)
        print(p.item)
        skriv(p.right)   


