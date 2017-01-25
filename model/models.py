from model.board import Board

class MineSweeper:
    def __init__(self):
        self.board = Board()

    def validate_position(self, position):
        self.board.markPosition(position)
        return self.board.get_board()
