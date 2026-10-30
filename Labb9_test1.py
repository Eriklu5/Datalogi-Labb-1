from LinkedQpeek import LinkedQ
from Labb9 import readformel
import unittest

from contextlib import redirect_stdout
from io import StringIO


class SyntaxTest(unittest.TestCase):

    def test_atom1(self):
        print("testar Na")
        with redirect_stdout(StringIO()) as buffer:
            readformel("Na\n")           
        self.assertEqual(buffer.getvalue(), "Formeln är syntaktiskt korrekt\n")

    def test_atom2(self):
        print("testar H2O")
        with redirect_stdout(StringIO()) as buffer:
            readformel("H2O\n")           
        self.assertEqual(buffer.getvalue(), "Formeln är syntaktiskt korrekt\n")

    def test_atom3(self):
        print("testar Si(C3(COOH)2)4(H2O)7")
        with redirect_stdout(StringIO()) as buffer:
            readformel("Si(C3(COOH)2)4(H2O)7\n")           
        self.assertEqual(buffer.getvalue(), "Formeln är syntaktiskt korrekt\n")

    def test_atom4(self):
        print("testar Na332")
        with redirect_stdout(StringIO()) as buffer:
            readformel("Na332\n")           
        self.assertEqual(buffer.getvalue(), "Formeln är syntaktiskt korrekt\n")

if __name__ == '__main__':
    unittest.main()