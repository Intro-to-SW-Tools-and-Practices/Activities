import unittest
from Game import BlackJack 
class Testing_Game(unittest.TestCase):
    def test_deal(self):
        game = BlackJack()
        hands = game.deal()
        self.assertEqual(len(hands),2)

    def test_calculate_values(self):
        game = BlackJack()
        hand = game.deal(1)
        hv = game.calculate_values(hand[0])
        self.assertEqual(type(hv),int)

if __name__ == '__main__':
    unittest.main()
