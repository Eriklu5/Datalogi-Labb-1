# Parse tree???

print("Formeln är syntaktiskt korrekt")
print("Saknad stor bokstav vid radslutet")
print("För litet tal vid radslutet")


""" 
    Föreläsning 13:
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
q = LinkedQ
molekyl = input()

while molekyl != "#": 
    q.append(molekyl)
    molekyl = input()


def läs_molekyl(molekyl):
    if molekyl == None: # Ska inte göras
        raise SyntaxError()
    läs_atom()
    läs_atom() and läs_num()
    

def läs_atom(atom):
    if atom == läs_LETTER:
        pass
    else: läs_letter() and läs_num()

def läs_LETTER(stor_bokstav):

    raise SyntaxError("")
def läs_letter(liten_bokstav):
    pass
def läs_num(siffra):
    pass

def readformel(kö):
    for element in kö:
        molekyl = kö.peek()
        if molekyl == läs_molekyl(molekyl):
            return


# Från labb 9:
def main():
    #stdin = open("indata1.txt") #Lätt att ändra för att testa indata från fil
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

main()



# Nästa, steg 4. 
""" Skriv ett testprogram med unittest som ska kontrollera
att dina funktioner fungerar som avsett. Se exempel från syntaxföreläsningen. 
T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl, 
som A -> a -> 5 (OBS! De fem funktionerna ska skrivas i nästa punkt.) """



import unittest

from syntax import *


class SyntaxTest(unittest.TestCase):

    def testSubjPred(self):
        """ Testar Subj och Pred """
        self.assertEqual(kollaGrammatiken("JAG VET"), "Följer syntaxen!")

    def testFelKonj(self):
        self.assertEqual(kollaGrammatiken("JAG VET MEN"), "Fel konjunktion: MEN före . ")

if __name__ == '__main__':
    unittest.main()



class SyntaxTest(unittest.TestCase):
    def test_syntax(self):
        self.assertEqual
        pass
    def test_fel(self):
        pass
    def test_korrekt_ordning(self):
        pass
        self.assertRaises(SyntaxError)


# Korrekt användning av varje funktion
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
        self.assertTrue(läs_LETTER())
        pass
    def test_letter(self):
        self.assertTrue(läs_letter())

        pass
    def test_num(self):
        self.assertTrue(läs_num())
        pass

# Steg 5. Implementera inläsningsmetoderna

from linkedQFile_Labb_8 import LinkedQ

# Frånn labb 8:
# Syntaxkontroll


class Syntaxfel(Exception):
    pass

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
        print(ordet, end = " ")
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


""" Om vi tittar på exemplen på felaktiga indata ser vi att utskriften av "den del av imatningen som är kvar" ser lite olika ut i de olika exemplen. Här är två exempel:
cr12	Saknad stor bokstav vid radslutet cr12
För detta fall kan man tjuvtitta (med peek()) på första tecknet "c" och direkt se att det inte är en stor bokstav - man behöver inte plocka ut det ur kön. Hela "cr12" finns kvar i kön och skrivs ut i felutskriften.

Men för att veta om det är fel räcker det inte alltid att bara titta ett tecken framåt. Betrakta följande exempel:

Pb1	För litet tal vid radslutet
Pb är en godkänd atom, så vi går vidare till siffrorna:
    Anropet av peek() ger oss "1", men vi måste gå vidare och se om det finns fler siffror, så vi plockar ut "1" ur kön med dequeue()
    Nu ser vi att det inte finns något kvar i kön, talet var alltså 1, så det är syntaxfel: För litet tal vid radslutet
    Vi skriver också ut resten av kön, men den är tom, så ettan kommer inte med i felutskriften. """


<Mening> ::= <Sats> | <Sats><Konj><Mening>
<Sats> ::= <Subj> <Pred>
<Subj> ::= JAG | DU
<Pred> ::= VET | TROR
<Konj> ::= ATT | OCH
<> icke-slutssymbol




Skriv funktionshuvud för fem funktioner, en för varje regel i syntaxen ovan. Funktionskroppen ska fyllas i senare, i punkt 5.
Gör en kopia av din LinkedQueue från labb 2, och lägg till metoden peek() som tittar på det första värdet i kön (det somfirst pekar på) utan att plocka ut det.
Gör ett eget särfall Syntaxfel som är subklass till (ärver från) Exception.
Skriv ett testprogram med unittest som ska kontrollera att dina funktioner fungerar som avsett. Se exempel från syntaxföreläsningen. T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl, som A -> a -> 5 (OBS! De fem funktionerna ska skrivas i nästa punkt.)
Lägg till kod i de fem funktionerna som kontrollerar syntaxen. Om en funktion upptäcker ett fel, tex Saknad stor bokstav eller För litet tal vid radslutet ska den göra raIse Syntaxfel(felmeddelande). Om allt gått bra gör funktionen inget.
Provkör med ditt testprogram.
Gå till Kattis och se till att ditt program klarar alla testfall! 



      
        



