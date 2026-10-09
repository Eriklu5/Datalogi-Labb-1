# Fortsättning av labb 8

from sys import stdin
from linkedQFile_Labb_8 import LinkedQ
import unittest



# BNF-syntax
""" 
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ... 
"""

# Utskrift 2
""" 
Okänd atom vid radslutet 4)5
Saknad siffra vid radslutet C
Saknad högerparentes vid radslutet
Felaktig gruppstart vid radslutet )Fe
För litet tal vid radslutet
För litet tal vid radslutet C
För litet tal vid radslutet 2C
Saknad stor bokstav vid radslutet cl
Saknad stor bokstav vid radslutet a
Felaktig gruppstart vid radslutet )3
Felaktig gruppstart vid radslutet )
Felaktig gruppstart vid radslutet 2
"""

# Möjliga utdata
"""
Antingen Formeln är syntaktiskt korrekt eller någon av följande felutskrifter
1. Okänd atom
2. Saknad siffra
3. Saknad högerparentes
4. Felaktig gruppstart
5. För litet tal
6. Saknad stor bokstav
7. Felaktig gruppstart
"""


# Kod

PERIODISKA= "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn Nh Fl  Mc Lv Ts Og"
periodiska = PERIODISKA.split()
print(periodiska)
print(len(periodiska))

# "Använd lämpligen rekursiv medåkning." Såsom man gör med beräkning av primtal? (Dvs vid sökning största primtal under x så beräknar man inte 2 till x varje iteration, 
# utan man sparar tidigare beräkning, dvs om x=100 och du räknat 50 av någon anledning, så itererar du din funktion mellan 51 och 101 istället för 2 till 50 + 2 till 101)



class Syntaxfel(Exception):
    pass


# Inläsningsmetoder

def readformel(kö):
    läs_mol(kö)
    # \n menas att syntaxen läser rad för rad endast en molekylformel i taget


def läs_mol(kö):
    läs_grupp(kö)
    if kö.peek() != None and kö.peek().isdigit():
        läs_mol(kö)


def läs_grupp(kö):
    if kö>1:
        läs_atom(kö)
        if kö.peek().isdigit():
            läs_num(kö)
    elif True:
        läs_mol(kö) # Måste kolla om () finns
        läs_num(kö)

            
def läs_atom(kö):
    läs_LETTER(kö)
    if kö.peek() != None and not kö.peek().isdigit():
        läs_letter(kö)


def läs_LETTER(kö):
    element = kö.peek()
    if (len(element) == 1 and "A" <= element <= "Z") or element.isupper():
        kö.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav")


def läs_letter(kö):
    element = kö.peek()
    if element.islower():
        kö.dequeue()
        return
    raise Syntaxfel("Saknad liten bokstav")


def läs_num(kö):
    siffra = kö.dequeue()
    if int(siffra) >= 2:
        return
    raise Syntaxfel("För litet tal")


# Huvudprogram

def main():
    stdin = open("Filer/indata2.txt")
    rad = stdin.readline()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:
            q.enqueue(tkn)
        try:
            readformel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            rest = ""
            while q.peek():
                rest += q.dequeue()
            print(felet, "vid radslutet", rest)
        rad = stdin.readline()
    stdin.close()
main()



# Kodtestning

class SyntaxTest(unittest.TestCase):
    # Allmän testning
    def test_input_1(self):
        q = LinkedQ()
        with open("Filer/indata1.txt", "r") as fil:
            rad = fil.readline()
            for tkn in rad:
                q.enqueue(tkn)
        self.assertEqual(readformel(q))


    def test_input_2(self):
        q = LinkedQ()
        with open("Filer/indata2.txt", "r") as fil:
            rad = fil.readline()
            for tkn in rad:
                q.enqueue(tkn)
        self.assertEqual(readformel(q))


    def test_fel(self):
        molekyl = ".K4"
        q = LinkedQ()
        for tkn in molekyl:
            q.enqueue(tkn)
        self.assertRaises("Saknad stor bokstav", readformel(q))

    # Korrekt användning av varje funktion

    def test_main(self):
        self.assertEqual(main(), print("Formeln är syntaktiskt korrekt"))

    def test_readformel(self):
        molekyl = "Li(Fe2S4)5Ag"
        q = LinkedQ()
        for tkn in molekyl:
            q.enqueue(tkn)
        self.assertEqual(readformel(q), None)

    def test_atom(self):
        atom = "Au"
        q = LinkedQ()
        for tkn in atom:
            q.enqueue(tkn)
        self.assertEqual(läs_atom(q), None)

    def test_LETTER(self):
        bokstav = "A"
        q = LinkedQ()
        q.enqueue(bokstav)
        self.assertEqual(läs_LETTER(q), None)

    def test_letter(self):
        bokstav = "a"
        q = LinkedQ()
        q.enqueue(bokstav)
        self.assertEqual(läs_letter(q), None)

    def test_num(self):
        nummer = "3"
        q = LinkedQ()
        q.enqueue(nummer)
        self.assertEqual(läs_num(q), None)


if __name__ == '__main__':
    unittest.main()