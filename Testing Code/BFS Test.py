import math
import pygame
<<<<<<< HEAD
=======
import time
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
# import networkx as nx

class Tile():
    def __init__(self):
        self.neighbours = []
        self.visited = False
        self.visited_order = -1
        element = None

class Board():
    def __init__(self, size):
<<<<<<< HEAD
        self.board = [[Tile() for r in range(9)] for c in range(9)]
=======
        self.board = [[Tile() for r in range(size)] for c in range(size)]
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
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

<<<<<<< HEAD
class Player():
=======
class Player(pygame.sprite.Sprite):
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
<<<<<<< HEAD

class Game():
    def __init__(self, num_players=4, size=9):
=======
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

class Game():
    def __init__(self, num_players, size):
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
        self.players = []
        colors = ['red', 'blue', 'yellow', 'green']
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        self.game_board = Board(size)

        for i in range(num_players):
            self.players.append(Player(colors[i], xpos[i], ypos[i]))
            self.game_board.board[ypos[i]][xpos[i]].element = self.players[i] 
<<<<<<< HEAD
=======
        self.all_sprite_list = pygame.sprite.Group()
    def printPlayer(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*100
            self.players[i].rect.y = (self.players[i].ypos)*100
            self.all_sprite_list.add(self.players[i])
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
 
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

<<<<<<< HEAD
def BFS(pos_ori, pos_dest, game):
=======
def BFS(game, pos_ori, pos_dest):
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    queque = []
    orden = 0
    queque.append(tile_org)
    while tile_org != tile_dest:
<<<<<<< HEAD
        tile_org = queque.pop(0)
        tile_org.visited_order = orden
        orden += 1

=======
        
        tile_org = queque.pop(0)
        tile_org.visited_order = orden
        orden += 1
        tile_org.visited = True
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
        for i in tile_org.neighbours:
            if i.visited == False:
                queque.append(i)
                i.visited = True
<<<<<<< HEAD
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)

=======
    
    
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)

def measure_time(sorting_alg, v):
  start = time.time()
  n = len(v)
  sorting_alg(v)
  end = time.time()
  return end-start
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91

def main():
    pygame.init()
    done = False
<<<<<<< Updated upstream
<<<<<<< HEAD
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    game = Game()
    pos_ori = [1,1]
    pos_dest = [3,3]
    BFS(pos_ori, pos_dest,game)
=======
    n = 11
=======
    n = 5
>>>>>>> Stashed changes
    numPlayer = 4
    SCREEN_WIDTH = int((n)*100)
    SCREEN_HEIGHT = int((n)*100)
    BLACK = (0,0,0)
    all_sprite_list = pygame.sprite.Group()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    game = Game(numPlayer, n)
    pos_ori = [1,1]
    pos_dest = [3,3]
    start = time.time()
    BFS(game, pos_ori, pos_dest)
    end = time.time()
    print(end-start)

    start = time.time()
    call_DFS(game, pos_ori, pos_dest)
    end = time.time()
    print(end-start)
>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill([255, 255, 255])
<<<<<<< HEAD
        for x in range(100,900,100):
            pygame.draw.line(screen,BLACK, (x,0),(x,900), 2)
        for y in range(100,900,100):
            pygame.draw.line(screen,BLACK, (0,y),(900,y), 2)
        pygame.display.flip()

=======
        for x in range(100,SCREEN_WIDTH,100):
            pygame.draw.line(screen,BLACK, (x,0),(x,SCREEN_WIDTH), 2)
        for y in range(100,SCREEN_HEIGHT,100):
            pygame.draw.line(screen,BLACK, (0,y),(SCREEN_HEIGHT,y), 2)

        game.printPlayer()
        game.all_sprite_list.draw(screen)
        pygame.display.flip()

        

>>>>>>> 2b44ad5e98086ed4d707bef4ccca48c5243a2d91
    pygame.quit()



if __name__== "__main__":
    main()

#DFS -- Akira



#BFS -- Cledmir


