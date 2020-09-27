import math
import pygame
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

class Player(pygame.sprite.Sprite):
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

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
        self.all_sprite_list = pygame.sprite.Group()
    def printPlayer(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*100
            self.players[i].rect.y = (self.players[i].ypos)*100
            self.all_sprite_list.add(self.players[i])
 
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
    orden = 0
    queque.append(tile_org)
    while tile_org != tile_dest:
        tile_org = queque.pop(0)
        tile_org.visited_order = orden
        orden += 1

        for i in tile_org.neighbours:
            if i.visited == False:
                queque.append(i)
                i.visited = True
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)


def main():
    pygame.init()
    done = False
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    all_sprite_list = pygame.sprite.Group()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    game = Game()
    pos_ori = [1,1]
    pos_dest = [3,3]
    BFS(pos_ori, pos_dest,game)

    for i in range(4):

        all_sprite_list.add()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill([255, 255, 255])
        for x in range(100,900,100):
            pygame.draw.line(screen,BLACK, (x,0),(x,900), 2)
        for y in range(100,900,100):
            pygame.draw.line(screen,BLACK, (0,y),(900,y), 2)

        game.printPlayer()
        game.all_sprite_list.draw(screen)
        pygame.display.flip()

        

    pygame.quit()



if __name__== "__main__":
    main()

#DFS -- Akira



#BFS -- Cledmir


