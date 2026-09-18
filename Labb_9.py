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




lista = []
molekyl = input()

while molekyl != "#": 
    lista.append(molekyl)
    molekyl = input()