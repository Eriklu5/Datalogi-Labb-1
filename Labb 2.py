#labb 2
from array import array
from arrayQFile import ArrayQ

def trolleri():
    kortlek = ArrayQ()
    kort_ordning_in = input("Vilken ordning ligger korten i? ")
    kort_ordning = kort_ordning_in.split(" ")
    for kort in kort_ordning:
        kortlek.enqueue(int(kort))
    print("De kommer ut i denna ordning: ",end="")
    while not kortlek.is_empty():
        kort_i_hand = kortlek.dequeue()
        kortlek.enqueue(kort_i_hand)
        print(kortlek.dequeue(),end=" ")

trolleri() # in-ordningen 3 1 5 2 4 ger ut-ordningen 1 2 3 4 5


