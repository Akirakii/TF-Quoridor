import math
# import networkx as nx

class Tile():
    def __init__(self):
        self.neighbors = []
        self.visited = False
        self.visited_order = -1
        self.is_shortest_path = False
        element = None

class Board():
    def __init__(self, size):
        self.board = [[Tile() for r in range(9)] for c in range(9)]
        self.indexing_tiles(self.board)

    def indexing_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j+1 < len(board[i]):
                    board[i][j].neighbors.append(board[i][j+1])
                if j-1 >= 0:
                    board[i][j].neighbors.append(board[i][j-1])
                if i-1 >= 0:
                    board[i][j].neighbors.append(board[i-1][j])
                if i+1 < len(board):
                    board[i][j].neighbors.append(board[i+1][j])

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
    for i in tile_ori.neighbors: 
        if i.visited == False: 
            DFS(i, tile_dest, visited_order+1)

def find_shortest_path(tile):
    tile.is_shortest_path = True
    if tile.visited_order == 0:
        return tile
    
    posible_targets = []
    
    minimum = min(i.visited_order for i in tile.neighbors if i.visited)
    for i in tile.neighbors:
        if i.visited_order == minimum:
            posible_targets.append(i) 

    if len(posible_targets) == 1:
        neighbor_target = posible_targets[0]
    else:
        neighbors_minimum = []
        for i in posible_targets:
            neighbor_minimum = min(i.visited_order for i in tile.neighbors if i.visited)
            neighbors_minimum.append(neighbor_minimum)

        minimum = min(i for i in neighbors_minimum)
        for i in tile.neighbors:
            if i.visited_order == minimum:
                neighbor_target = i

    find_shortest_path(neighbor_target)


def call_DFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    DFS(tile_org, tile_dest, 0)
    find_shortest_path(tile_dest)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_path(board_util)
    game.game_board.reset_tiles(board_util)

game = Game()
pos_ori = [1,1]
pos_dest = [3,3]
call_DFS(game, pos_ori, pos_dest)


