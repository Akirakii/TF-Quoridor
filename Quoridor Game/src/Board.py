import Tile

class Board():
    def __init__(self, size):
        self.board = [[Tile.Tile() for r in range(size)] for c in range(size)]
        self.indexing_tiles(self.board)

    def indexing_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j+1 < len(board[i]):
                    board[i][j].neighbours.append(board[i][j+1])
                if j-1 >= 0:
                    board[i][j].neighbours.append(board[i][j-1])
                if i-1 >= 0:
                    board[i][j].neighbours.append(board[i-1][j])
                if i+1 < len(board):
                    board[i][j].neighbours.append(board[i+1][j])

    def print_visited_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j].visited_order
                print(v, end = ",  " if v in range(0,9) else ", ")
            print("\n")
    
    def print_path(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(1 if board[i][j].is_shortest_path else 0, end = ",  ")
            print("\n")

    def reset_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].visited = False
                board[i][j].visited_order = -1
                board[i][j].is_shortest_path = False