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

        if self.root == None:
            self.root = putta(self.root,newvalue)

        elif newvalue < self.root.item:

            self.root.left.put(newvalue)


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

    else: 
        p

def finns(p,value):
    pass





def skriv(p):
    pass




svenska = Bintree()              # Skapa ett trädobjekt
svenska.put("gurka")		    # Sortera in "gurka" i trädet	
print(svenska.root.item)
""" 
if "gurka" in svenska:           # Kolla om "gurka" finns i trädet
            - - -                        # (Operatorn in anropar metoden __contains__ 
                                            # som du ska implementera i din Bintree-klass)
            
svenska.write()                  # Skriver alla trädobjektets ord i bokstavsordning
 """