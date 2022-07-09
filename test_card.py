import unittest
from Card import Card
class Testing_card(unittest.TestCase):
    def test_to_String(self):
        card = Card(1,1)
        self.assertEqual(type(card.to_String()), type("string"))

    def test_get_value(self):
        card = Card(1,1)
        self.assertEqual(card.get_value(), '1')

    def test_get_value2(self):
        card = Card(0,1)
        self.assertEqual(card.get_value(), '1')

if __name__ == '__main__':
    unittest.main()
