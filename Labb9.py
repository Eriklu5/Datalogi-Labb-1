from LinkedQpeek import LinkedQ

from sys import stdin

PERIODISKA = "H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn Nh Fl  Mc Lv Ts Og"
periodiska = PERIODISKA.split()


def take_input():
    rad = stdin.readline()
    while rad[0] != "#":
        readformel(rad)
        rad = stdin.readline()
    stdin.close()


def readformel(molekyl): # Tar in ett molekylnamn och kollar om det är syntaktiskt korrekt    
    molekylkö = LinkedQ()
    for tkn in molekyl:
        molekylkö.enqueue(tkn)
    try:
        läs_formel(molekylkö) 
        print("Formeln är syntaktiskt korrekt")
    except Syntaxfel as felet:
        rest = ""
        while molekylkö.peek() != "\n":
            rest += molekylkö.dequeue()
        print(felet, "vid radslutet", rest)


"""
<formel>::= <mol> \n
<mol>   ::= <group> | <group><mol>
<group> ::= <atom> |<atom><num> | (<mol>) <num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
"""

def läs_formel(kö):
    # \n menas att i syntaxen läses molekyler rad för rad endast en i taget
    # readline() gör så att i slutet finns \n vilket också läggs in i kön
    while kö.peek() != "\n" and kö.peek() != None:
        # Denna loop ska alltid fånga \n före None, annars är det ett Syntaxfel
        läs_molekyl(kö)
    if kö.peek() == None:
        raise Syntaxfel("Inget rad avslut")






def läs_molekyl(kö):
    # Syntaxen hanterar inte mol, dvs antal mol, varje molekyl antas bara vara 1 mol inte flera
    # Mol signifierar istället endast hur många grupper som finns i molekylen, grupp +? grupp +? grupp...
    läs_grupp(kö)
    if kö.peek() != "\n" and kö.peek() != ")":
        läs_molekyl(kö)


def läs_grupp(kö):
    # En grupp börjar alltid antingen med parantes eller stor bokstav, annars Syntaxfel
    # eftersom mol skulle ha hanterat eventuell siffra vid start som vid 6H20 (men detta förekommer inte)
    while kö.peek() != "\n":

        if kö.peek().isalpha():
            läs_atom(kö)
            if kö.peek().isdigit():
                läs_num(kö)
            return

        elif kö.peek() == "(":
            kö.dequeue()    # Vad händer om CH()4, den raisar Saknad stor siffra!!!
            while kö.peek() != ")" and kö.peek() != "\n" and kö.peek() != None: # Denna fångar inte, därför får man oändlig rekursion vid mol()
                läs_molekyl(kö)

            if kö.peek() == ")":
                kö.dequeue()
                if kö.peek().isdigit():
                    läs_num(kö)
                    return
                raise Syntaxfel("Saknad siffra")

            raise Syntaxfel("Saknad högerparentes")

        raise Syntaxfel("Felaktig gruppstart")



def läs_atom(kö):
    # Varje atom ges som antingen 1 enskild stor bokstav eller tillsammans med 1 liten bokstav
    S_bokstav = läs_LETTER(kö)
    if kö.peek().islower():
        L_bokstav = läs_letter(kö)
        if S_bokstav + L_bokstav in periodiska:
            return
        raise Syntaxfel("Okänd atom")

    if S_bokstav in periodiska:
        return
    raise Syntaxfel("Okänd atom")

def läs_LETTER(kö):
    element = kö.peek()
    if (len(element) == 1 and "A" <= element <= "Z") or element.isupper():
        kö.dequeue()
        return element
    raise Syntaxfel("Saknad stor bokstav")

def läs_letter(kö):
    element = kö.peek()
    if element.islower():
        kö.dequeue()
        return element
    raise Syntaxfel("Saknad liten bokstav")

def läs_num(kö):
    siffra = kö.dequeue()
    if int(siffra) > 0:

        nummer = siffra
        while kö.peek().isdigit():
            siffra = kö.dequeue()
            nummer += siffra  #konkatenerar strings

        if int(nummer) >= 2:
            return
    raise Syntaxfel("För litet tal")


class Syntaxfel(Exception):
    pass


def main():
    take_input()

if __name__ == "__main__":
    main()