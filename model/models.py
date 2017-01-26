from model.board import Board


class MineSweeper:
    def __init__(self):
        self._board = Board((3, 3))

    def validate_position(self, position):
        return self._board.mark_position(position)

    def get_elements_size(self):
        return self._board.get_elements_size()

    def get_board(self):
        return self._board.get_board()
