from model.board import Board

class MineSweeper:
    def __init__(self):
        self.board = Board()

        rows = []
        for x in range(1,4):
            buttons = []
            for y in range(1,4):
                buttons.append({'position': 'position_{}_{}'.format(x, y)})

            rows.append({'buttons': buttons})

        self.minestable = {'rows': rows}

    def validate_position(self, position):
        self.board.markPosition(position)
        return self.board.get_board()
