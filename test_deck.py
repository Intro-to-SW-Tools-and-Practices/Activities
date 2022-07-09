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
        DeckSize = len(D.cards)
        card  = D.draw()
        card2 = D.draw()
        # Make Sure the PoP is giving us different cards
        self.assertNotEqual(card, card2)

        #Make sure our Deck is decreasing in size as we pop.
        self.assertEqual(len(D.cards),(DeckSize - 2))

if __name__ == '__main__':
    unittest.main()
