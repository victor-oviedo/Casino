import random
import numpy as np


def score(to_score):

    result = list(map(lambda x: 10 if x in [0, 10, 11, 12] else x, to_score))

    if(sum(list(map(lambda x: 11 if x == 1 else x, result))) == 21 and len(to_score)==2):
        print('BlackJack!')
        return 21
    else:
        return sum(result)

    



def player_hand(hand,isOpening=False):
    """Shows each player hand and figures out score"""
    h =  '|' #hand
    
    to_score = []

    for k in hand:
        
        q = k%13 #Each suit has 13 cards
        to_score.append(q)

        if(isOpening==False or k!=hand[-1]):

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

        else:
            h+= "X|"

    if 'X' not in h:
        score(to_score)

    print(h)

    return score(to_score)



def table(player,crupier, isOpening=False):
    """Shows the table"""
    print("*"*50)
    player_hand(crupier,isOpening)
    print("\n")
    player_hand(player)
    print("*"*50+"\n")

    return None



def deck(cards_on_table):
    """Generates one card and appends to the list cards_on_table"""

    card = cards_on_table[0]
    while card in cards_on_table:
        card = random.randint(1,52) #deck of cards
    cards_on_table.append(card)

    return cards_on_table



def run():

    cards_on_table = []
    cards_on_table.append(random.randint(1,52)) #first card

    for i in range(3): #Opening
        deck(cards_on_table)

    opening = np.array_split(cards_on_table,2)
    player = list(opening[0])
    crupier = list(opening[1])
    table(player,crupier,True)

    escor = 18
    bj = '89'

    while(player_hand(player)<21 and 'BlackJack' not in bj):
        jugar = int(input('Wanna play?: '))
        if(jugar == 1):
        
            card = deck(cards_on_table)
            player.append(cards_on_table[-1])
            table(player,crupier,True)
        escor = escor + 1

    table(player,crupier) #Final player's table
    
    #crupier's game

    while(player_hand(crupier)<=16 and player_hand(crupier)<21):
            card = deck(cards_on_table)
            crupier.append(cards_on_table[-1])       
            table(player,crupier)  

    return None


run()