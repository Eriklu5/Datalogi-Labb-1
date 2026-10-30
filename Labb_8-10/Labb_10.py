from molgrafik import *
from linkedQFile_Labb_8 import LinkedQ

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Labb_7.hashtest import lagraHashtabell
from Labb_7.hashtest import skapaAtomlista



PERIODISKA = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn Nh Fl  Mc Lv Ts Og"
periodiska = PERIODISKA.split()


class Syntaxfel(Exception):
    pass


# Inläsningsmetoder

def readformel(kö):
    # \n menas att i syntaxen läses molekyler rad för rad endast en i taget
    # readline() gör så att i slutet finns \n vilket också läggs in i kön
    while kö.peek() != "\n" and kö.peek() != None:
        # Denna loop ska alltid fånga \n före None, annars är det ett Syntaxfel
        färdig_struktur = läs_mol(kö) # Det första Ruta objektet blir returnerat
        return färdig_struktur
    if kö.peek() == None:
        raise Syntaxfel("Inget rad avslut")


def läs_mol(kö):
    # Syntaxen hanterar inte mol, dvs antal mol, varje molekyl antas bara vara 1 mol inte flera
    # Mol signifierar istället endast hur många grupper som finns i molekylen, grupp +? grupp +? grupp...
    mol = läs_grupp(kö) # Ruta objekt med atom | atom num

    if kö.peek() != "\n" and kö.peek() != ")":
        mol.next = läs_mol(kö) # Läs mol returnerar mol, vilket är ett Ruta objekt, så Ruta.next = Ruta. Nod struktur
    return mol


def läs_grupp(kö):
    # En grupp börjar alltid antingen med parantes eller stor bokstav, annars Syntaxfel
    # eftersom mol skulle ha hanterat eventuell siffra vid start som vid 6H20 (men detta förekommer inte)
    rutan = Ruta()
    while kö.peek() != "\n":

        if kö.peek().isalpha():
            atom = läs_atom(kö)
            rutan.atom = atom # num krävs inte, bas fall är alltid 1

            if kö.peek().isdigit():
                num = läs_num(kö)
                rutan.num = num
            return rutan

        elif kö.peek() == "(":
            kö.dequeue()    # Vad händer om CH()4, den raisar Saknad stor siffra!!!
            while kö.peek() != ")" and kö.peek() != "\n" and kö.peek() != None: # Denna fångar inte, därför får man oändlig rekursion vid mol()
                delmolekyl = läs_mol(kö)
                rutan.down = delmolekyl

            if kö.peek() == ")":
                kö.dequeue()
                if kö.peek().isdigit():
                    läs_num(kö)
                    return 
                raise Syntaxfel("Saknad siffra")

            raise Syntaxfel("Saknad högerparentes")

        raise Syntaxfel("Felaktig gruppstart")


def läs_atom(kö):
    # Varje atom ges som antingen 1 enskild stor bokstav eller tillsammans med 1 liten bokstav
    S_bokstav = läs_LETTER(kö)
    if kö.peek().islower():
        L_bokstav = läs_letter(kö)
        if S_bokstav + L_bokstav in periodiska:
            return S_bokstav + L_bokstav
        raise Syntaxfel("Okänd atom")

    if S_bokstav in periodiska:
        return S_bokstav
    raise Syntaxfel("Okänd atom")


def läs_LETTER(kö):
    element = kö.peek()
    if (len(element) == 1 and "A" <= element <= "Z") or element.isupper():
        kö.dequeue()
        return element
    raise Syntaxfel("Saknad stor bokstav")


def läs_letter(kö):
    element = kö.peek()
    if element.islower():
        kö.dequeue()
        return element
    raise Syntaxfel("Saknad liten bokstav")


def läs_num(kö):
    siffra = kö.dequeue()
    if int(siffra) > 0:

        nummer = siffra
        while kö.peek().isdigit():
            siffra = kö.dequeue()
            nummer += siffra  #konkatenerar strings

        if int(nummer) >= 2:
            return nummer
    raise Syntaxfel("För litet tal")


def weight(molekyl):
    # Vikten för molekyl är vikten för grupper, vikten för grupper är vikten för atomer, vikten för atomer är Atomnamnets specifika vikt gånger nummret 

    hashtabell = lagraHashtabell()
        # Key är atomnamnet, "C", nyckeln är Atom, Atom.namn = namn, Atom.vikt = vikt
        # Sök upp vikten för varje atom genom att söka efter key, vikt är Atom.vikt




    grupp = molekyl.split()
    weight(grupp)


    molekyl_vikt = 0

    for i in molekyl: # måste dela upp denna i varje atom del
        atom = hashtabell.search(i)
        if i == atom.namn:
            molekyl_vikt += atom.vikt

    return molekyl_vikt






# Huvudprogram

def main():
    stdin = open("Filer/indata2.txt")
    rad = stdin.readline()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:  # Eftersom allt i raden läggs i kön måste readformel avgöra när molekylen är färdig
            # och när resterande ger syntaxfel, det ska vara en sammanhängande rad utan mellanslag komma osv
            q.enqueue(tkn)
        try:
            mol = readformel(q)
            print("Formeln är syntaktiskt korrekt")
            mg = Molgrafik
            mg.show(mol)
            # vikt = weight(q)
            # print("Molekyls vikt är: ", vikt)
        except Syntaxfel as felet:
            rest = ""
            while q.peek() != "\n":
                rest += q.dequeue()
            print(felet, "vid radslutet", rest)
        rad = stdin.readline()
    stdin.close()


""" if __name__ == "__main__":
    main() """


import unittest

class SyntaxTest(unittest.TestCase):

    def test_Grafik(self):
        print("Kollar en korrekt atom")
        atomkö = LinkedQ()
        for tkn in "C(OH)2\n":
            atomkö.enqueue(tkn)
        molekyl = readformel(atomkö)
        mg = Molgrafik()
        abba = mg.show(molekyl)
        self.assertTrue(abba)


if __name__ == '__main__':
    unittest.main()


# Exempel:
""" 
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
 """









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