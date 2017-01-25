from model.board import Board

class MineSweeper:

    def validate_position(self, position):
        board = Board()
        board.markPosition(position)
        return board.get_board()
