import unittest
from Deck import Deck 
class Testing_deck(unittest.TestCase):

    #Test the shuffle command
    def test_shuffle(self):
        D = Deck()
        D.shuffle()
        self.assertNotEqual(D.cards[1], D.cards[0])

    #Test Card value to ensure its being correctly stored
    def test_draw(self):
        D = Deck()
        card = D.draw()
        self.assertEqual(card, card)

    #Test Draw to see if POP is working
    def test_draw_pop(self):
        D = Deck()
        card = D.draw()
        card2 = D.draw()
        self.assertNotEqual(card, card2)

if __name__ == '__main__':
    unittest.main()
