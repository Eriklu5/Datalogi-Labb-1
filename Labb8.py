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
        if self.__first.data == None:
            return False
        return self.__first.data




"""
    <group> ::= <atom> | <atom><num>
    <atom>  ::= <LETTER> | <LETTER><letter>
    <LETTER>::= A | B | C | ... | Z
    <letter>::= a | b | c | ... | z
    <num>   ::= 2 | 3 | 4 | ...
"""


def läs_molekyl(molekyl):
    läs_atom(molekyl)
    if molekyl.peek() != None:
        läs_num(molekyl)

def läs_atom(atom):
    läs_LETTER(atom)
    if atom.peek() == "liten bokstav":
        läs_letter(atom)

def läs_LETTER(stor_bokstav):
    if stor_bokstav.peek() in ["A","B","C","D","...etc"]:
        stor_bokstav.dequeue()
        return
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet")

def läs_letter(liten_bokstav):
    if liten_bokstav.peek() in ["a","b","c","d","...etc"]:
        liten_bokstav.dequeue()
        return
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet") # Varför ska den säga så känns märkligt men det finns inget fall för ex: BD2

def läs_num(siffra):
    if siffra.peek() >= 2:
        siffra.dequeue()
        return
    else:
        raise SyntaxError("För litet tal vid radslutet")
 

class Syntaxfel(Exception):
    pass


import unittest

class SyntaxTest(unittest.TestCase):

    def testläs_num(self):
        self.assertEqual(läs_num(5))
        with self.assertRaises(SyntaxError):
            läs_num("1")


    def testSyntaxRätt(self):
        molekyl = "H2"
        q = LinkedQ()
        for tkn in molekyl:
            q.enqueue(tkn)

        self.assertEqual(readformel(q), "Formeln är syntaktiskt korrekt") # readfomel tar en kö och kollar om molekylen är syntaktiskt korrekt

    def testSyntaxFel(self):
        self.assertEqual(main("cr12"), "Saknad stor bokstav vid radslutet cr12")

if __name__ == '__main__':
    unittest.main()


hej = "hej"
hej.isupper()