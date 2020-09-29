import Tile

class Board():
    def __init__(self, size):
        board = []
        for y in range(size):
            board.append([])
            for x in range(size):
                board[y].append(Tile.Tile(y, x))

        self.board = board
        self.indexing_tiles()

    def indexing_tiles(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j+1 < len(self.board[i]):
                    self.board[i][j].neighbours.append(self.board[i][j+1])
                if j-1 >= 0:
                    self.board[i][j].neighbours.append(self.board[i][j-1])
                if i-1 >= 0:
                    self.board[i][j].neighbours.append(self.board[i-1][j])
                if i+1 < len(self.board):
                    self.board[i][j].neighbours.append(self.board[i+1][j])

    def print_visited_tiles(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                v = self.board[i][j].visited_order
                print(v, end = ",  " if v in range(0,9) else ", ")
            print("\n")
    
    def print_path(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(1 if self.board[i][j].is_shortest_path else 0, end = ",  ")
            print("\n")

    def reset_tiles(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].visited = False
                self.board[i][j].visited_order = -1
                self.board[i][j].is_shortest_path = False