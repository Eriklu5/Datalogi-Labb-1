from LinkedQpeek import LinkedQ
from Labb9 import readformel
import unittest

from contextlib import redirect_stdout
from io import StringIO


class SyntaxTest(unittest.TestCase):
    def test_atom1(self):
        print("testar C(Xx4)5")
        with redirect_stdout(StringIO()) as buffer:
            readformel("C(Xx4)5\n")           
        self.assertEqual(buffer.getvalue(), "Okänd atom vid radslutet 4)5\n")

    def test_atom2(self):
        print("testar C(OH4)C")
        with redirect_stdout(StringIO()) as buffer:
            readformel("C(OH4)C\n")           
        self.assertEqual(buffer.getvalue(), "Saknad siffra vid radslutet C\n")

    def test_atom3(self):
            print("testar C(OH4C")
            with redirect_stdout(StringIO()) as buffer:
                readformel("C(OH4C\n")           
            self.assertEqual(buffer.getvalue(), "Saknad högerparentes vid radslutet \n")

    def test_atom4(self):
        print("testar H2O)Fe")
        with redirect_stdout(StringIO()) as buffer:
            readformel("H2O)Fe\n")           
        self.assertEqual(buffer.getvalue(), "Felaktig gruppstart vid radslutet )Fe\n")
        
    def test_atom5(self):
        print("testar H0")
        with redirect_stdout(StringIO()) as buffer:
            readformel("H0\n")           
        self.assertEqual(buffer.getvalue(), "För litet tal vid radslutet \n")

    def test_atom6(self):
        print("testar H1C")
        with redirect_stdout(StringIO()) as buffer:
            readformel("H1C\n")           
        self.assertEqual(buffer.getvalue(), "För litet tal vid radslutet C\n")

    def test_atom7(self):
        print("testar H02C")
        with redirect_stdout(StringIO()) as buffer:
            readformel("H02C\n")           
        self.assertEqual(buffer.getvalue(), "För litet tal vid radslutet 2C\n")

    def test_atom8(self):
        print("testar Nacl")
        with redirect_stdout(StringIO()) as buffer:
            readformel("Nacl\n")           
        self.assertEqual(buffer.getvalue(), "Saknad stor bokstav vid radslutet cl\n")

    def test_atom9(self):
        print("testar a")
        with redirect_stdout(StringIO()) as buffer:
            readformel("a\n")           
        self.assertEqual(buffer.getvalue(), "Saknad stor bokstav vid radslutet a\n")

    def test_atom10(self):
        print("testar (Cl)2)3")
        with redirect_stdout(StringIO()) as buffer:
            readformel("(Cl)2)3\n")           
        self.assertEqual(buffer.getvalue(), "Felaktig gruppstart vid radslutet )3\n")

    def test_atom11(self):
        print("testar )")
        with redirect_stdout(StringIO()) as buffer:
            readformel(")\n")           
        self.assertEqual(buffer.getvalue(), "Felaktig gruppstart vid radslutet )\n")

    def test_atom12(self):
        print("testar 2")
        with redirect_stdout(StringIO()) as buffer:
            readformel("2\n")           
        self.assertEqual(buffer.getvalue(), "Felaktig gruppstart vid radslutet 2\n")


if __name__ == '__main__':
    unittest.main()