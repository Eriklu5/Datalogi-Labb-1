# Labb 2. pverison
from linkedQFile import LinkedQ



def trolleri():

    spel = LinkedQ()
    start_ordning = input()
    start_ordning = start_ordning.strip().split()

    for siffra in start_ordning:
        spel.enqueue(siffra)


    while not spel.isEmpty():
        första_kort = spel.dequeue()

        spel.enqueue(första_kort)

        print(spel.dequeue())


trolleri()