import unittest
from model.models import MineSweeper


class TestStringMethods(unittest.TestCase):

    def test_not_mine(self):
        mine_sweeper = MineSweeper()
        self.assertEqual(mine_sweeper.has_mine((0,0)), False)

    def test_mine(self):
        mine_sweeper = MineSweeper()
        self.assertEqual(mine_sweeper.has_mine((1,1)), True)


if __name__ == '__main__':
    unittest.main()
