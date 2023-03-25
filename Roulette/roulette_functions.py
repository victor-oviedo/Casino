import numpy as np

def board():
    """Print board and options"""

    board = """
          __________ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
         /    |  3  |  6  |  9  |  12 |  15 |  18 |  21 |  24 |  27 |  30 |  33 |  36 |
        |  0  |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
        |_____|  2  |  5  |  8  |  11 |  14 |  17 |  20 |  23 |  26 |  29 |  32 |  35 |
        |     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
        | 00  |  1  |  4  |  7  |  10 |  13 |  16 |  19 |  22 |  25 |  28 |  31 |  34 |
        |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

        Number  Bet               Profit             Number  Bet                  Profit
        ------------------------------------------------------------------------------
        1.      From 1 to 18        1X               12.     Column5 [15,14,13]     11X
        2.      From 19 to 36       1X               13.     Column6 [18,17,16]     11X
        3.      Even numbers        1X               14.     Column7 [21,20,19]     11X
        4.      Odd numbers         1X               15.     Column8 [24,23,22]     11X
        5.      Row1 [3,6,...,36]   2X               16.     Column9 [27,26,25]     11X
        6.      Row2 [2,5,...,35]   2X               17.     Column10 [30,29,28]    11X
        7.      Row3 [1,4,...,34]   2X               18.     Column11 [33,32,31]    11X
        8.      Column1 [3,2,1]     11X              19.     Column12 [36,35,34]    11X
        9.      Column2 [6,5,4]     11X              20.     Two numbers            17X 
        10.     Column3 [9,8,7]     11X              21.     One number             35X   
        11.     Column4 [12,11,10]  11X              
        """
    print(board)




def select_game(bet_number,valid_number=True):
    """Defines bet and profit"""

    x = np.arange(1,37) #numbers from 1 to 36

    if(bet_number=='1'):
        bet = np.array_split(x,2)[0]
        profit = 1
    elif(bet_number=='2'):
        bet = np.array_split(x,2)[1]
        profit = 1
    elif(bet_number=='3'):
        bet = list(filter(lambda v: v % 2 == 0, x))
        profit = 1
    elif(bet_number=='4'):
        bet = list(filter(lambda v: v % 2 == 1, x))
        profit = 1
    elif(bet_number=='5'):
        bet = list(filter(lambda v: v % 3 == 0, x))
        profit = 2
    elif(bet_number=='6'):
        bet = list(filter(lambda v: (v+1) % 3 == 0, x))
        profit = 2
    elif(bet_number=='7'):
        bet = list(filter(lambda v: (v+2) % 3 == 0, x))
        profit = 2
    elif(bet_number=='8'):
        bet = [3,2,1]
        profit = 11
    elif(bet_number=='9'):
        bet = [6,5,4]
        profit = 11
    elif(bet_number=='10'):
        bet = [9,8,7]
        profit = 11
    elif(bet_number=='11'):
        bet = [12,11,10]
        profit = 11
    elif(bet_number=='12'):
        bet = [15,14,13]
        profit = 11
    elif(bet_number=='13'):
        bet = [18,17,16]
        profit = 11
    elif(bet_number=='14'):
        bet = [21,20,19]
        profit = 11
    elif(bet_number=='15'):
        bet = [24,23,22]
        profit = 11
    elif(bet_number=='16'):
        bet = [27,26,25]
        profit = 11
    elif(bet_number=='17'):
        bet = [30,29,28]
        profit = 11
    elif(bet_number=='18'):
        bet = [33,32,31]
        profit = 11
    elif(bet_number=='19'):
        bet = [36,35,34]
        profit = 11
    elif(bet_number=='20'):
        bet = numbers_from_input(bet_number)
        profit = 17
    elif(bet_number=='21'):
        bet = numbers_from_input(bet_number)
        profit = 35
    else:
        bet = []; profit=0
        valid_number = False
        print("Please enter a valid option")

    return bet, profit, valid_number


def validation(ball, numbers):
    "Validates win or lose"

    if(ball in numbers):
        print('Win!\n')
        return True
    else:
        print('Lose!\n')
        return False
    

def new_capital(capital, bet_value, result, profit):
    "Cañculates new capital"
    if(result):
        return capital + profit*bet_value
    else:
        return capital - bet_value
    

def numbers_from_input(bet_number):
    "Validates input"
    from_input = []

    n1_validation = False; n2_validation = False
    while(n1_validation==False or n2_validation == False):
        n1_validation = False
        n2_validation = False
        n1 = input("Enter a number: ")
        if(n1=='00'):
            n1 = 37

        if(bet_number=='20'): #two numbers
            n2 = input("Enter another: ")
            if(n2=='00'):
                n2 = 37
            while(n1 == n2):
                print("Both numbers are equal ")
                n2 = input("Enter second number: ")
        else:
            n2_validation = True

        try:
            n1 = int(n1)
            if(bet_number=='20'):
                n2 = int(n2)  

        except ValueError:
            print("Please, enter valid numbers")  

        else: 
            if(n1 in np.arange(0,38)):
                n1_validation = True
            if(bet_number=='20' and n2 in np.arange(0,38)):
                n2_validation = True
            if(n1_validation==False or (bet_number=='20' and n2_validation==False)):
                print("Please, enter valid numbers") 



    from_input.append(n1)
    if(bet_number=='20'):
        from_input.append(n2)
        
    return from_input
