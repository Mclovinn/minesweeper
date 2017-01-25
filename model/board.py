class Board:
    bombs = [(1,1)]
    size = [(3,3)]
    board = {(0,0):'', (1,0):'', (2,0):'', (0,1):'', (1,1):'', (2,1):'', (0,2):'', (1,2):'', (2,2):''}

    def markPosition(self, position):
        state = 'NOT_BOMB'

        if (position in Board.bombs):
            state = 'BOMB'

        Board.board[position] = state

    def get_board(self):
        return Board.board
