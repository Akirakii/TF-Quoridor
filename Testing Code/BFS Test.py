import math
# import networkx as nx

class Tile():
    def __init__(self):
        self.neighbours = []
        self.visited = False
        self.visited_order = -1
        element = None

class Board():
    def __init__(self, size):
        self.board = [[Tile() for r in range(9)] for c in range(9)]
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

    def set_all_visited_false(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].visited = False
                board[i][j].visited_order = -1

class Player():
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos

class Game():
    def __init__(self, num_players=4, size=9):
        self.players = []
        colors = ['red', 'blue', 'yellow', 'green']
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        self.game_board = Board(size)

        for i in range(num_players):
            self.players.append(Player(colors[i], xpos[i], ypos[i]))
            self.game_board.board[ypos[i]][xpos[i]].element = self.players[i] 
 
 #DFS
def DFS(tile_ori, tile_dest, visited_order):
    tile_ori.visited = True
    tile_ori.visited_order = visited_order
    if tile_dest.visited == True:
        return
    for i in tile_ori.neighbours: 
        if i.visited == False: 
            DFS(i, tile_dest, visited_order+1)


def call_DFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    DFS(tile_org, tile_dest, 0)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)

def BFS(pos_ori, pos_dest, game):
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    queque = []
    queque.append(tile_org)
    while tile_org != tile_dest:
        tile_org = queque.pop(0)
        tile_org.visited_order += 1

        for i in tile_org.neighbour:
            if i.visited == False:
                queque.append(i)
                i.visited = True
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)


def main():
    game = Game()
    pos_ori = [1,1]
    pos_dest = [3,3]
    #call_DFS(game, pos_ori, pos_dest)
    BFS(pos_ori, pos_dest,game)


if __name__== "__main__":
    main()

#DFS -- Akira



#BFS -- Cledmir


