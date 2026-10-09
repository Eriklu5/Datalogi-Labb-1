# Parse tree???

""" Rules to Draw a Parse Tree
All leaf nodes need to be terminals.
All interior nodes need to be non-terminals.
In-order traversal gives the original input string. """

from linkedQFile_Labb_8 import LinkedQ
from syntax import *
import unittest
from lark import Lark

grammar = r""" 
     <molekyl> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...
    Labb 8:
      <group> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...

 """



""" Rules to Draw a Parse Tree
All leaf nodes need to be terminals.
All interior nodes need to be non-terminals.
In-order traversal gives the original input string. """


# Inläsningsmetoder


def läs_atom(kö_data):
    läs_LETTER(kö_data)
    if kö_data.peek().islower():
        läs_letter(kö_data)


def läs_LETTER(kö_data):
    # is upper kollar om alla bokstäver är stora och det finns något,
    # men vi vet att endast ett element (bokstav eller siffra) kollas åt gången så detta utgör inget problem
    element = kö_data.peek()
    if (len(element) == 1 and "A" < element < "Z") or element.isupper():
        kö_data.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav")


def läs_letter(kö_data):
    kö_data.dequeue()
    # raise Syntaxfel("Saknad stor bokstav")


def läs_num(kö_data):
    if int(kö_data.peek()) < 2:
        kö_data.dequeue()
        while kö_data.peek() != None:
            läs_num(kö_data)
        raise Syntaxfel("För litet tal")
    return


""" Om vi tittar på exemplen på felaktiga indata ser vi att utskriften av "den del av imatningen som är kvar" ser lite olika ut i de olika exemplen. Här är två exempel:
cr12	Saknad stor bokstav vid radslutet cr12
För detta fall kan man tjuvtitta (med peek()) på första tecknet "c" och direkt se att det inte är en stor bokstav - man behöver inte plocka ut det ur kön. Hela "cr12" finns kvar i kön och skrivs ut i felutskriften.

Men för att veta om det är fel räcker det inte alltid att bara titta ett tecken framåt. Betrakta följande exempel:

Pb1	För litet tal vid radslutet
Pb är en godkänd atom, så vi går vidare till siffrorna:
    Anropet av peek() ger oss "1", men vi måste gå vidare och se om det finns fler siffror, så vi plockar ut "1" ur kön med dequeue()
    Nu ser vi att det inte finns något kvar i kön, talet var alltså 1, så det är syntaxfel: För litet tal vid radslutet
    Vi skriver också ut resten av kön, men den är tom, så ettan kommer inte med i felutskriften. """


def readformel(kö):
    while kö.peek() != None:
        if kö.peek().isdigit():
            läs_num(kö)
        elif isinstance(kö.peek(), str):
            läs_atom(kö)

    return


""" 
# Från labb 9:
def main():
    # stdin = open("indata1.txt") #Lätt att ändra för att testa indata från fil
    rad = stdin.readline()
    while rad[0] != "#":
        q = LinkedQ()
        for tkn in rad:
            q.enqueue(tkn)
        try:
            readformel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as felet:
            rest = str(q).strip()
            print(felet, "vid radslutet", rest)
        rad = stdin.readline()


main() """


class SyntaxTest(unittest.TestCase):
    # Allmän testning
    def test_syntax(self):
        self.assertEqual
        pass
    def test_fel(self):
        pass

    def test_korrekt_ordning(self):
        pass
        self.assertRaises(SyntaxError)

    # Korrekt användning av varje funktion
""" 
    def test_main(self):
        self.assertEqual(main(), print("Formeln är syntaktiskt korrekt"))
        pass

    def test_readformel(self):
        self.assertEqual(readformel())

    def test_molekyl(self):
        molekyl = H2SO4
        self.assertTrue(läs_molekyl(molekyl))
        pass

    def test_atom(self):
        self.assertTrue(läs_atom())
        pass

    def test_LETTER(self):
        bokstav = "A"
        self.assertTrue(läs_LETTER(bokstav), "Det stämmer")

    def test_letter(self):
        self.assertTrue(läs_letter())

        pass

    def test_num(self):
        self.assertTrue(läs_num())
        pass """


if __name__ == '__main__':
    unittest.main()


# Frånn labb 8:
# Syntaxkontroll

""" 
<Mening > : := <Sats > | < Sats > <Konj > <Mening >
<Sats >: := <Subj > <Pred >
<Subj >: := JAG | DU
<Pred >: := VET | TROR
<Konj >: := ATT | OCH
<> icke-slutssymbol """


def läsMening(ordkö):
    läsSats(ordkö)
    if ordkö.peek() == ".":
        ordkö.dequeue()
    else:
        läsKonj(ordkö)
        läsMening(ordkö)


def läsSats(ordkö):
    läsSubj(ordkö)
    läsPred(ordkö)


def läsSubj(ordkö):
    ordet = ordkö.dequeue()
    if ordet == "JAG":
        return
    if ordet == "DU":
        return
    raise Syntaxfel("Fel subjekt: " + ordet)


def läsPred(ordkö):
    ordet = ordkö.dequeue()
    if ordet == "TROR":
        return
    if ordet == "VET":
        return
    raise Syntaxfel("Fel predikat: " + ordet)


def läsKonj(ordkö):
    ordet = ordkö.dequeue()
    if ordet == "ATT":
        return
    if ordet == "OCH":
        return
    raise Syntaxfel("Fel konjunktion: " + ordet)


def skrivut(ordkö):
    while not ordkö.isEmpty():
        ordet = ordkö.dequeue()
        print(ordet, end=" ")
    print()


def lagraMening(mening):
    ordkö = WordQueue()
    mening = mening.split()
    for ordet in mening:
        ordkö.enqueue(ordet.upper())
    ordkö.enqueue(".")
    return ordkö


def kollaGrammatiken(ordkö):
    try:
        läsMening(ordkö)
        return "Följer syntaxen!"
    except Syntaxfel as fel:
        return str(fel) + " före " + str(ordkö)


def main():
    mening = input(" - Skriv en mening: ")
    while mening:
        ordkö = lagraMening(mening)
        resultat = kollaGrammatiken(ordkö)
        print(resultat)
        mening = input(" - Skriv en mening: ")


if __name__ == "__main__":
    main()
