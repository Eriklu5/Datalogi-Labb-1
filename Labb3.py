
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



        #self.root = putta(self.root,newvalue)




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
    
    elif p.item < newvalue: # om värdet är samma så läggs det till höger borde kanske ha ett specialfall?
        p.left = putta(p.left,newvalue)
        return p
    else:
        p.right = putta(p.right,newvalue)
        return p

def finns(p,value):
    pass





def skriv(p):
    pass




svenska = Bintree()              # Skapa ett trädobjekt
svenska.put("morot")

print(svenska.root.item)		    # Sortera in "gurka" i trädet
svenska.put("gurka")

print(svenska.root.right.item)
svenska.put("sallad")

print(svenska.root.left.item)


""" 
if "gurka" in svenska:           # Kolla om "gurka" finns i trädet
            - - -                        # (Operatorn in anropar metoden __contains__ 
                                            # som du ska implementera i din Bintree-klass)
            
svenska.write()                  # Skriver alla trädobjektets ord i bokstavsordning
 """