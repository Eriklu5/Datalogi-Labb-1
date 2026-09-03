#labb 2
from linkedQFile import LinkedQ

def trolleri(): 
    kortlek = LinkedQ()
    kort_ordning_in = input()
    kort_ordning = kort_ordning_in.strip().split(" ")
    for kort in kort_ordning:
        kortlek.enqueue(kort)
    while not kortlek.isEmpty():
        kort_i_hand = kortlek.dequeue()
        kortlek.enqueue(kort_i_hand)
        print(kortlek.dequeue(),end=" ")

trolleri() # in-ordningen 3 1 5 2 4 ger ut-ordningen 1 2 3 4 5


