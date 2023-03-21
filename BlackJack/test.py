import blackjack_functions
import unittest

class BlackBoxTest(unittest.TestCase):


    def test_validation(self):
        game = {'player': 10, 'crupier': 15}
        t1 = blackjack_functions.validation(game)
        self.assertEqual(t1,'You lose!')

        game['player'] = 15
        t2 = blackjack_functions.validation(game)
        self.assertEqual(t2,'Push!')

        game['player'] = 16
        t3 = blackjack_functions.validation(game)
        self.assertEqual(t3,'You win!')

        game['crupier'] = 25
        t4 = blackjack_functions.validation(game)
        self.assertEqual(t4,'You win!')     

        game = {'player': 25, 'crupier': 15}
        t5 = blackjack_functions.validation(game)
        self.assertEqual(t5,'You lose!') 


    def test_best_result(self):
        t1 = blackjack_functions.best_result([1,6])
        self.assertEqual(t1,17)

        t2 = blackjack_functions.best_result([10,1])
        self.assertEqual(t2,21)

        t3 = blackjack_functions.best_result([9,10,1])
        self.assertEqual(t3,20)


    def test_deck(self):
        import numpy as np
        cards = list(np.arange(1,52))
        t1 = blackjack_functions.deck(cards)
        self.assertEqual(t1,list(np.arange(1,53)))



if __name__ == '__main__':
    unittest.main()