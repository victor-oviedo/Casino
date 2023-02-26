import random
import numpy as np


def player_hand(hand):

    h =  '|' #hand

    for k in hand:

        q = k%13 #13 cards has each suit

        if(q==1):
            h += 'A|'
        elif(q==11):
            h += 'J|'
        elif(q==12):
            h += 'Q|'
        elif(q==0):
            h += 'K|'
        else:
            h+= str(q) + "|"

    return h



def table(player,crupier):

    print("*"*50)
    print(player_hand(crupier))
    print("\n")
    print(player_hand(player))
    print("*"*50+"\n")
    return None


def deck(cards_on_table):

    card = cards_on_table[0]
    #print(card)
    while card in cards_on_table:
        card = random.randint(1,52) #deck of cards
    cards_on_table.append(card)

    return cards_on_table



def run():

    cards_on_table = []
    cards_on_table.append(random.randint(1,52))

    for i in range(3): #Opening
        deck(cards_on_table)


    opening = np.array_split(cards_on_table,2)
    player = list(opening[0])
    crupier = list(opening[1])
    print(player,crupier)

    table(player,crupier)

    return None


run()