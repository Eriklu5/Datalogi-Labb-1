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

# Givna möjliga utdata, där # Klar (Labb, ordning)
"""
Antingen Formeln är syntaktiskt korrekt eller någon av följande felutskrifter
1. Okänd atom               # Klar (9,1)
2. Saknad siffra            # Klar (9,3)
3. Saknad högerparentes     # Klar (9,4)
4. Felaktig gruppstart      # Klar (9,2)
5. För litet tal            # Klar (8)
6. Saknad stor bokstav      # Klar (8)
7. Saknad liten bokstav     # Klar (8)
"""


# Kod

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
        läs_mol(kö)
    if kö.peek() == None:
        raise Syntaxfel("Inget rad avslut")


def läs_mol(kö):
    # Syntaxen hanterar inte mol, dvs antal mol, varje molekyl antas bara vara 1 mol inte flera
    # Mol signifierar istället endast hur många grupper som finns i molekylen, grupp +? grupp +? grupp...
    läs_grupp(kö)
    if kö.peek() != "\n" and kö.peek() != ")":
        läs_mol(kö)


def läs_grupp(kö):
    # En grupp börjar alltid antingen med parantes eller stor bokstav, annars Syntaxfel
    # eftersom mol skulle ha hanterat eventuell siffra vid start som vid 6H20 (men detta förekommer inte)
    while kö.peek() != "\n":

        if kö.peek().isupper():
            läs_atom(kö)
            if kö.peek().isdigit():
                läs_num(kö)
            return kö.peek()

        elif kö.peek() == "(":
            kö.dequeue()    # Vad händer om CH()4
            if kö.peek() != ")":
                while kö.peek() != ")" and kö.peek() != "\n" and kö.peek() != None: # Denna fångar inte, därför får man oändlig rekursion vid mol()
                    läs_mol(kö)

                if kö.peek() == ")":
                    kö.dequeue()
                    if kö.peek().isdigit():
                        läs_num(kö)
                    raise Syntaxfel("Saknad siffra")
                
                raise Syntaxfel("Saknad högerparantes")

            raise Syntaxfel("Saknad innehåll")

        raise Syntaxfel("Felaktig gruppstart")


def läs_atom(kö):
    # Varje atom ges som antingen 1 enskild stor bokstav eller tillsammans med 1 liten bokstav
    S_bokstav = läs_LETTER(kö)
    if kö.peek().islower():
        L_bokstav = läs_letter(kö)
        if S_bokstav + L_bokstav in periodiska:
            return kö.peek()
        raise Syntaxfel("Okänd atom")

    if S_bokstav in periodiska:
        return kö.peek()
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
    if int(siffra) >= 2:
        return
    raise Syntaxfel("För litet tal")


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

# Testa med (CH3)2C3H6, (CH_3)_2 C_3 H_6

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
        self.assertRaises(Syntaxfel, readformel, q)

    # Korrekt användning av varje funktion

    def test_main(self):
        self.assertEqual(main(), print("Formeln är syntaktiskt korrekt"))

    def test_readformel(self):
        molekyl = "Li(Fe2S4)5Ag"
        q = LinkedQ()
        for tkn in molekyl:
            q.enqueue(tkn)
        self.assertEqual(readformel(q), None)

    def test_mol(self):
        pass

    def test_grupp(self):
        pass

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
        self.assertEqual(läs_LETTER(q), "A")

    def test_letter(self):
        bokstav = "a"
        q = LinkedQ()
        q.enqueue(bokstav)
        self.assertEqual(läs_letter(q), "a")

    def test_num(self):
        nummer = "3"
        q = LinkedQ()
        q.enqueue(nummer)
        self.assertEqual(läs_num(q), None)


if __name__ == '__main__':
    unittest.main()
