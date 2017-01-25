class MineSweeper:
    bombs = [(1,1)]
    size = [(3,3)]

    def has_mine(self, position):
        return position in MineSweeper.bombs
