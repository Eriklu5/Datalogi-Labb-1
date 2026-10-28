from Labb_9 import *


class SyntaxTest(unittest.TestCase):

    def test_input_1(self):
        self.assertEqual(main("Filer/indata1.txt"), None)


    def test_input_2(self):
        self.assertEqual(main("Filer/indata2.txt"), None)


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
