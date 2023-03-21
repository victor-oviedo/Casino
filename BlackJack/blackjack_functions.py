import numpy as np
import random

def validation(dic_score):
    """Defines who wins"""

    if(dic_score['player']>21):
        return 'You lose!'

    elif(dic_score['crupier']>21):
        return 'You win!'

    else: 
        if(dic_score['player']>dic_score['crupier']):
            return 'You win!'
        
        elif(dic_score['player']==dic_score['crupier']):
            return 'Push!'

        else:
            return 'You lose!'



def best_result(result):
    """Decides if A is 1 or 11"""
    if(sum(result)+10<=21):
        return sum(result)+10 #Soft 17 for crupier
    else:
        return sum(result)



def score(to_score,dic_score,who_is):
    """Counts cards value"""

    result = list(map(lambda x: 10 if x in [10, 11, 12, 0] else x, to_score))

    if(sum(list(map(lambda x: 11 if x == 1 else x, result))) == 21 and len(to_score)==2):
        print('BlackJack!')
        dic_score[who_is] = 21
    elif(1 in result):
        dic_score[who_is] = best_result(result)
    else:
        dic_score[who_is] = sum(result)
    
    return None



def player_hand(hand, dic_score, who_is, isOpening=False):
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

    score(to_score,dic_score,who_is)
    return h



def table(player,crupier, dic_score, isOpening=False):
    """Shows the table"""
    print("*"*50)
    print(player_hand(crupier, dic_score, 'crupier',isOpening=isOpening))
    print("\n")
    print(player_hand(player, dic_score, 'player'))
    print("*"*50+"\n")

    return None



def deck(cards_on_table):
    """Generates one card and appends to the list cards_on_table"""

    card = cards_on_table[0]
    while card in cards_on_table:
        card = random.randint(1,52) #deck of cards
    cards_on_table.append(card)

    return cards_on_table


