import random
import numpy as np


def best_result(result):
    if(sum(result)+10<=21):
        return sum(result)+10 #Soft 17 for crupier
    else:
        return sum(result)



def score(to_score,dic_score,who_is):

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

    #if 'X' not in h:
     #   score(to_score)

    #print(h)

    #return score(to_score)

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



def run():

    cards_on_table = []
    cards_on_table.append(random.randint(1,52)) #first card
    
    dic_score = {'player': 0, 'crupier': 0} #to save scores
    hand_score = 0

    for i in range(3): #Opening
        deck(cards_on_table)

    opening = np.array_split(cards_on_table,2)
    player = list(opening[0])
    crupier = list(opening[1])
    table(player,crupier, dic_score, True)


    print(dic_score)

    #player game
    jugar = 1
    while(dic_score['player']<21 and jugar==1):   
        jugar = int(input("""Another card? \n 0: No \n 1: Yes \n"""))
        if(jugar == 1):
        
            card = deck(cards_on_table)
            player.append(cards_on_table[-1])
            table(player,crupier,dic_score, True)

    #crupier's game
    while(dic_score['crupier']<=16 and dic_score['crupier']<21 and dic_score['player']<=21):
            card = deck(cards_on_table)
            crupier.append(cards_on_table[-1])       
            table(player, crupier, dic_score)  
    

    return None


run()

