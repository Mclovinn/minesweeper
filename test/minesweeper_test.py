import unittest
from model.models import MineSweeper


class TestStringMethods(unittest.TestCase):

    def test_not_mine(self):
        position = (0,0)

        mine_sweeper = MineSweeper()
        board = mine_sweeper.validate_position(position)
        self.assertEqual(9, len(board))

        self.assertEqual('NOT_BOMB', board[position])

    def test_mine(self):
        position = (1,1)

        mine_sweeper = MineSweeper()
        board = mine_sweeper.validate_position(position)
        self.assertEqual(9, len(board))

        self.assertEqual('BOMB', board[position])

if __name__ == '__main__':
    unittest.main()
