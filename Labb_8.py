# Parse tree???

print("Formeln är syntaktiskt korrekt")
print("Saknad stor bokstav vid radslutet")
print("För litet tal vid radslutet")


""" 

      <molekyl> ::= <atom> | <atom><num>
      <atom>  ::= <LETTER> | <LETTER><letter>
      <LETTER>::= A | B | C | ... | Z
      <letter>::= a | b | c | ... | z
      <num>   ::= 2 | 3 | 4 | ...

 """



""" Om vi tittar på exemplen på felaktiga indata ser vi att utskriften av "den del av imatningen som är kvar" ser lite olika ut i de olika exemplen. Här är två exempel:
cr12	Saknad stor bokstav vid radslutet cr12
För detta fall kan man tjuvtitta (med peek()) på första tecknet "c" och direkt se att det inte är en stor bokstav - man behöver inte plocka ut det ur kön. Hela "cr12" finns kvar i kön och skrivs ut i felutskriften.

Men för att veta om det är fel räcker det inte alltid att bara titta ett tecken framåt. Betrakta följande exempel:

Pb1	För litet tal vid radslutet
Pb är en godkänd atom, så vi går vidare till siffrorna:
    Anropet av peek() ger oss "1", men vi måste gå vidare och se om det finns fler siffror, så vi plockar ut "1" ur kön med dequeue()
    Nu ser vi att det inte finns något kvar i kön, talet var alltså 1, så det är syntaxfel: För litet tal vid radslutet
    Vi skriver också ut resten av kön, men den är tom, så ettan kommer inte med i felutskriften. """

peek()


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



        
class Node:
    # Skapar en nod som innehåller ett värde och pekar på nästa nod, annars på none
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQ:
    """Skapar en länkad lista av noder 
    \n Metoder: 
    \n  def enqueue(any) lägger till element i kö
    \n  def dequeue(any) returerar element först i kö
    \n  def isEmpty() kollar om det finns ett första element, returerar True eller False """
    def __init__(self):
        self.__first = None
        self.__last = None


    def enqueue(self, data):
        # Lägger till, två fall, första om listan är tom annars om den inte är det
        if self.__first == None:
            self.__first = Node(data)
            self.__last = self.__first
        else:
            self.__last.next = Node(data)
            self.__last = self.__last.next

    def dequeue(self):
        # Tar bort första noden och returnar dess värde, om den är tom så returnar None istället
        first = self.__first

        if self.isEmpty(): 
            return None
        
        elif self.__first == self.__last:
            self.__first = None
            self.__last = None

        else: 
            self.__first = self.__first.next

        return first.data

    def isEmpty(self):
        # Kollar om det finns ett första element, om inte är den tom
        if self.__first == None:
            return True
        else:
            return False

    def peek(self):
        return self.__first.data



class Syntaxfel(Exception):
    pass

        

lista = []
molekyl = input()

while molekyl != "#": 
    lista.append(molekyl)
    molekyl = input()







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