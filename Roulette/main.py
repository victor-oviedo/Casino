import random
import roulette_functions


def run():
    play = '1'
    money = 100
    bet_value = 0.0
    while(play=='1' and money > 0):
        roulette_functions.board()
        print(f"Capital {money} USD")

        valid_number = False
        while(valid_number == False):
            bet_number = input("Enter a number for your bet: ")
            numbers, profit, valid_number =  roulette_functions.select_game(bet_number)

        bet_value = ''
        while(type(bet_value) != float):
            bet_value = input("Enter bet value [$]: ")

            try:
                bet_value = float(bet_value)
            except ValueError:
                pass
            else:
                if(bet_value>money):
                    print("Enter a valid amount")
                    bet_value = ''

            
        ball = random.randint(0,37)
        if(ball == 37):
            print('-'*39, '> 00 <', '-'*39) 
        else:
            print('-'*39, '>', ball, '<', '-'*39) 
        
        result = roulette_functions.validation(ball, numbers)

        money = roulette_functions.new_capital(money, bet_value, result, profit)
        print(f"Capital {money} USD")        

        if(money>0):
            play = input("Another game?\n Yes: Enter 1 \n No:  Enter anything ")
            if(play != '1'):
                break


    return None


if __name__ == '__main__':
    run()