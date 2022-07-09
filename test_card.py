import unittest
from Card import Card
class Testing_Card(unittest.TestCase):
    def Test_To_String(self):
        card = Card(1,1)
        self.assertEqual(type(card.to_String()), type("string"))

    def Test_Get_Value(self):
        card = Card(1,1)
        self.assertEqual(card.get_value(), '2')

    def Test_Get_Value2(self):
        card = Card(0,1)
        self.assertEqual(card.get_value(), 'Ace')

if __name__ == '__main__':
    unittest.main()
