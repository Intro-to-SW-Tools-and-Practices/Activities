import unittest
from main import Main

class Test_Main(unittest.TestCase):
    def test_main(self):
        main()
        self.assrtEquals(True, True)