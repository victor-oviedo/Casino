import random
import numpy as np
import blackjack_functions

def run():

    cards_on_table = []
    cards_on_table.append(random.randint(1,52)) #first card
    
    dic_score = {'player': 0, 'crupier': 0} #to save scores

    for i in range(3): #Opening
        blackjack_functions.deck(cards_on_table)

    opening = np.array_split(cards_on_table,2)
    player = list(opening[0])
    crupier = list(opening[1])
    blackjack_functions.table(player,crupier, dic_score, True)
    
    #player's game
    while(dic_score['player']<21): 
        jugar = '2'
        while(jugar != '1' and jugar!='0'):
            jugar = input("Another card? \n 0: No \n 1: Yes \n")

        if(jugar == '1'):
            card = blackjack_functions.deck(cards_on_table)
            player.append(cards_on_table[-1])
            blackjack_functions.table(player,crupier,dic_score, True)

        if(jugar == '0'):
            break


    #crupier's game
    covered_card = True
    while(dic_score['crupier']<=16 and dic_score['crupier']<21 and dic_score['player']<=21):
            card = blackjack_functions.deck(cards_on_table)
            crupier.append(cards_on_table[-1])       
            blackjack_functions.table(player, crupier, dic_score)  
            covered_card = False

    if(covered_card == True): #to show crupier's last card
        blackjack_functions.table(player, crupier, dic_score)
    

    print(blackjack_functions.validation(dic_score))

    return None


if __name__ == '__main__':
    run()