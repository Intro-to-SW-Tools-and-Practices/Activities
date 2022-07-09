import unittest
from Deck import Deck 
class Testing_deck(unittest.TestCase):
    def test_shuffle(self):
        D = Deck()
        D.shuffle()
        self.assertNotEqual(D.cards[1], D.cards[0])

    def test_draw(self):
        D = Deck()
        card = D.draw()
        self.assertEqual(card, card)

if __name__ == '__main__':
    unittest.main()
