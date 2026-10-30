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
    if kö.peek() != None and kö.peek().isdigit():
        läs_num(kö)


def läs_atom(kö):
    läs_LETTER(kö)
    if kö.peek() != None and kö.peek().islower():
        läs_letter(kö)


def läs_LETTER(kö):
    element = kö.peek()
    if element.isupper():
        # (len(element) == 1 and "A" <= element <= "Z")
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
    if int(siffra) == 1 and kö.peek() != None and kö.peek().isdigit():
        return
    raise Syntaxfel("För litet tal")



# Feltestning


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
            readformel(atomkö)


    def test_SyntaxRätt(self):
        print("Kollar en korrekt atom")
        atomkö = LinkedQ()
        for tkn in "P21":
            atomkö.enqueue(tkn)
        self.assertEqual(readformel(atomkö),None)


if __name__ == '__main__':
    unittest.main()




def main():
    rad = input()
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
        rad = input()


if __name__ == "__main__":
    main()
