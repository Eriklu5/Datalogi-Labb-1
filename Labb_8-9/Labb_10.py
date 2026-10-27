from molgrafik import *
from linkedQFile_Labb_8 import LinkedQ
from Labb_7.hashtable import Hashtable
from Labb_7.hashtest import lagraHashtabell



#Bygger upp träd för "C(OH)2"
ruta1 = Ruta("C")
ruta2 = Ruta(num=2)
ruta1.next = ruta2
ruta3 = Ruta("O")
ruta2.down = ruta3
ruta4 = Ruta("H")
ruta3.next = ruta4

molekyl = ruta1

mg = Molgrafik()
mg.show(molekyl)


class Syntaxfel(Exception):
    pass


def readatom():
    pass


def readnum(kö):
    siffra = kö.dequeue()
    if int(siffra) >= 2:
        return siffra
    raise Syntaxfel("För litet tal")


def readgroup():
    rutan = Ruta()
    atom = readatom()
    num = readnum()

    rutan.atom = atom
    rutan.num = num

    # Om det är en parantes så ska
    rutan.num = num
    delmolekyl = readmol() # Som det görs i labb 9
    rutan.down = delmolekyl

    return rutan 


def readmol():
    # Denna tar in en grupp i taget från readgroup, dvs en nod i taget
    mol = readgroup()
    if .peek() != "\n":
        mol.next() = readgroup()
    return # Första noden


def readformel():
    mol = readmol()
    return # Första noden


def weight(mol):
    """ Molekylvikten ska beräknas rekursivt med anropet weight(mol). 
    Formulera först en mycket rekursiv tanke för vikten och programmera den sedan! 
    Låt programmet skriva ut vikten av molekylen i terminalfönstret. """

    hashtabell = lagraHashtabell()
        # Key är atomnamnet, "C", nyckeln är Atom, Atom.namn = namn, Atom.vikt = vikt
        # Sök upp vikten för varje atom genom att söka efter key, vikt är Atom.vikt

    molekyl_vikt = 0

    for i in mol: # måste dela upp denna i varje atom del
        atom = hashtabell.search(i)
        if i == atom.namn:
            molekyl_vikt += atom.vikt

    return molekyl_vikt


def main():
    q = LinkedQ
    q.enqueue(readformel())
    mol = q.dequeue()

    mg = Molgrafik
    mg.show(mol)

    vikt = weight(mol)
    print("Molekyls vikt är: ", vikt)






# =============== Pseudokod =================


# === Klasser ===

# Klassen Molgrafik (1/2) är en redskap för att grafiskt representera atomen
# Denna klass skrivs själv



# Klassen Ruta (2/2) är egentligen bara en nod trots namnet. Den har två pekare nedåt och till sidan
# Hela koden är given i specifikationen


# === Funktioner === 

# Funktionen weight ska beräkna vikten av hela molekylen
# vilket troligtvis är en instans av klassen Ruta
# Därav behöver man beräkna vikten av varje atom en efter en genom .next, .down
# 
# def weight(mol): 
#   vikt = mol.atom * mol.num * specifik vikt för själva atomen
    # "(Tips: I testprogrammet hashtest.py från hashlabben finns alla atomvikter.)"
#   return vikt + weight(mol.next)

# def readformel(kö)
#   

# === Huvudprogram ===

# Huvudprogrammet main() ska utföra en rad operationer: 
# 1. läs in en rad av en molekyl eller atom, input("Molekyl: ")
# 2. bryt ned denna rad i delar utefter syntaxen med readformel() som anropar resterande funktioner
# 3. representera denna molekyl som en nod med pekare på varje del, som en naturlig process av programmet
# 4. beräkna vikten av denna molekyl genom weight(mol)
# 5. grafiskt representera denna med hjälp av metoden Molgrafik.show(mol)