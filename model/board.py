class Board:
    bombs = [(1,1)]

    def __init__(self, size):
        self.size = size
        self._board = dict()
        self._rows = list()

        self._init_board()

    def _init_board(self):
        for x in range(self.size[0]):
            row = list()
            for y in range(self.size[1]):
                self._board[(x, y)] = ''
                row.append((x, y))

            self._rows.append(row)

    def get_size(self):
        return self.size

    def get_elements_size(self):
        return self.size[0] * self.size[1]

    def mark_position(self, position):
        state = 'NOT_BOMB'

        if (position in Board.bombs):
            state = 'BOMB'

        self._board[position] = state

        return state

    def _build_id(self, position):
        return 'position_{}_{}'.format(*position)

    def get_board(self):
        rows = list()
        for row in self._rows:
            new_row = list()
            print (row)
            for col in row:
                new_row.append((self._board[col], self._build_id(col)))
            rows.append(row)

        return {'rows': rows}
