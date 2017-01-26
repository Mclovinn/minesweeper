import unittest
from model.models import MineSweeper
from model.board import Board


class TestStringMethods(unittest.TestCase):
    def test_board_size(self):
        mine_sweeper = MineSweeper()
        self.assertEqual(9, mine_sweeper.get_elements_size())

    def test_not_mine(self):
        position = (0,0)
        mine_sweeper = MineSweeper()
        state = mine_sweeper.validate_position(position)
        self.assertEqual('NOT_BOMB', state)

    def test_mine(self):
        position = (1,1)
        mine_sweeper = MineSweeper()
        state = mine_sweeper.validate_position(position)
        self.assertEqual('BOMB', state)

    def test_board_1(self):
        board = Board((3, 3))
        self.assertEqual(board.get_size(), (3, 3))

    def test_board_2(self):
        board = Board((3, 3))
        result_board = board.get_board()
        self.assertIsInstance(result_board['rows'], list)

    def test_board_3(self):
        board = Board((3, 3))
        result_board = board.get_board()
        for row in result_board['rows']:
            self.assertIsInstance(row, list)

    def test_board_4(self):
        board = Board((3, 3))
        result_board = board.get_board()
        for row in result_board['rows']:
            self.assertIsInstance(row, list)


if __name__ == '__main__':
    unittest.main()
