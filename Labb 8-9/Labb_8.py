# Parse tree???

""" Rules to Draw a Parse Tree
All leaf nodes need to be terminals.
All interior nodes need to be non-terminals.
In-order traversal gives the original input string. """

from linkedQFile_Labb_8 import LinkedQ
# from syntax import *
import unittest
# from lark import Lark

grammar = r""" 
     <molekyl> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...
 """


class Syntaxfel(Exception):
    pass


# Inläsningsmetoder

def readformel(kö):
    läs_atom(kö)
    if kö.peek().isdigit():
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



""" Om vi tittar på exemplen på felaktiga indata ser vi att utskriften av "den del av imatningen som är kvar" ser lite olika ut i de olika exemplen. Här är två exempel:
cr12	Saknad stor bokstav vid radslutet cr12
För detta fall kan man tjuvtitta (med peek()) på första tecknet "c" och direkt se att det inte är en stor bokstav - man behöver inte plocka ut det ur kön. Hela "cr12" finns kvar i kön och skrivs ut i felutskriften.

Men för att veta om det är fel räcker det inte alltid att bara titta ett tecken framåt. Betrakta följande exempel:

Pb1	För litet tal vid radslutet
Pb är en godkänd atom, så vi går vidare till siffrorna:
    Anropet av peek() ger oss "1", men vi måste gå vidare och se om det finns fler siffror, så vi plockar ut "1" ur kön med dequeue()
    Nu ser vi att det inte finns något kvar i kön, talet var alltså 1, så det är syntaxfel: För litet tal vid radslutet
    Vi skriver också ut resten av kön, men den är tom, så ettan kommer inte med i felutskriften. """


class SyntaxTest(unittest.TestCase):
    # Feltestning

    def test_fel(self):
        molekyl = "KK4"
        q = LinkedQ()
        for tkn in molekyl:
            q.enqueue(tkn)
        self.assertRaises(Syntaxfel, readformel, q)

        with self.assertRaises(Syntaxfel):
            readformel(q)


    # Korrekt användning av varje funktion

    """ def test_main(self):

        self.assertEqual(main(), print("Formeln är syntaktiskt korrekt")) """

    def test_readformel(self):
        molekyl = "H2SO4"
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
