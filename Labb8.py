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
    \n  def isEmpty() kollar om det finns ett första element, returerar True eller False 
    \n  def peek() kollar på den första i kön och returnerar dess data"""
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
        if self.__first == None: # Är listan tom returneras None som data
            return None
        return self.__first.data


"""
    Syntaktiska regler
    <group> ::= <atom> | <atom><num>
    <atom>  ::= <LETTER> | <LETTER><letter>
    <LETTER>::= A | B | C | ... | Z
    <letter>::= a | b | c | ... | z
    <num>   ::= 2 | 3 | 4 | ...
"""

def readformel(molekyl): # Tar in ett molekylnamn och kollar om det är syntaktiskt korrekt
    molekylkö = LinkedQ()
    for tkn in molekyl:
        molekylkö.enqueue(tkn)
    try:
        läs_molekyl(molekylkö) 
        print("Formeln är syntaktiskt korrekt")
    except Syntaxfel as felet:
        rest = ""
        while not molekylkö.isEmpty():
            rest += molekylkö.dequeue()
        print(felet, "vid radslutet", rest)


def läs_molekyl(molekyl): # Namnet är lite missvisande eftersom funktionen just nu bara läser homonukleära molkyler
    läs_atom(molekyl)
    if molekyl.peek() != None:
        läs_num(molekyl)

def läs_atom(atom):
    läs_LETTER(atom)
    if atom.peek() != None:
        if not atom.peek().isdigit():
            läs_letter(atom)

def läs_LETTER(stor_bokstav):
    if stor_bokstav.peek().isupper():
        stor_bokstav.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav")

def läs_letter(liten_bokstav):
    if liten_bokstav.peek().islower():
        liten_bokstav.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav") # Varför ska den säga så känns märkligt men det finns inget fall för ex: BD2

def läs_num(siffra): 
    if not siffra.peek().isdigit() or siffra.peek() == "0": #Om det inte är en siffra är det fel
        siffra.dequeue() 
        raise Syntaxfel("För litet tal") # Bör skilja på fallen om man lägger till fler felmeddelnaden
    if siffra.peek() == "1": # Kollar nästa
        siffra.dequeue()
        if siffra.peek() != None: 
            if siffra.peek().isdigit(): # om nästa är ett tal så är formeln ok
                return
        raise Syntaxfel("För litet tal")
    return # Om den var ett tal som inte var 0 eller 1 så är den >2 vilket var regeln


class Syntaxfel(Exception):
    pass



"""
import unittest

class SyntaxTest(unittest.TestCase):

    def test_läs_num(self):
        print("Kollar läs_num")
        atomkö = LinkedQ()
        atomkö.enqueue("5")
        self.assertEqual(läs_num(atomkö),None) # när nummret >= 2
        atomkö.dequeue()
        atomkö.enqueue("1")
        with self.assertRaises(Syntaxfel): # när nummret < 2
            läs_num(atomkö)
        atomkö.enqueue("1")
        atomkö.enqueue("1")
        self.assertEqual(läs_num(atomkö),None) # när nummret >= 2 men måste kolla nästa siffra


    def test_läs_letter(self):
        print("Kollar läs_letter")
        atomkö = LinkedQ()
        atomkö.enqueue("a")
        atomkö.enqueue("B")
        self.assertEqual(läs_letter(atomkö),None)
        with self.assertRaises(Syntaxfel):
            läs_letter(atomkö)

    def test_läs_LETTER(self):
        print("Kollar läs_LETTER")
        atomkö = LinkedQ()
        atomkö.enqueue("A")
        atomkö.enqueue("b")
        self.assertEqual(läs_LETTER(atomkö),None)
        with self.assertRaises(Syntaxfel):
            läs_LETTER(atomkö)

    def test_SyntaxFel(self):
        print("Kollar en felaktig atom")
        atomkö = LinkedQ()
        for tkn in "cr12":
            atomkö.enqueue(tkn)
        with self.assertRaises(Syntaxfel):
            läs_molekyl(atomkö)

    def test_SyntaxRätt(self):
        print("Kollar en korrekt atom")
        atomkö = LinkedQ()
        for tkn in "P21":
            atomkö.enqueue(tkn)
        self.assertEqual(läs_molekyl(atomkö),None)

if __name__ == '__main__':
    unittest.main()
"""

# Inmatning 
indata = input()
while indata != "#":
    readformel(indata)
    indata = input()