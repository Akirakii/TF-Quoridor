import math
import pygame
import time

class Tile():
    def __init__(self):
        self.neighbours = []
        self.visited = False
        self.visited_order = -1
        self.is_shortest_path = False
        element = None

class Board():
    def __init__(self, size):
        self.board = [[Tile() for r in range(size)] for c in range(size)]
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

class Player(pygame.sprite.Sprite):
    def __init__(self, color, xpos, ypos, goal):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.goal = goal
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def move(self, board):
        for indx, i in board[self.goal[indx][0]][self.goal[indx][1]]:
            if board[self.xpos][self.ypos] == i:
                return
        for indx, i in board[self.xpos][self.ypos].neighbours:
            if i.is_shortest_path == True:
                if indx == 0:
                    self.xpos += 1 
                elif indx == 1:
                    self.xpos -= 1 
                elif indx == 2:
                    self.ypos -= 1 
                elif indx == 3:
                    self.ypos += 1 



class Game():
    def __init__(self, num_players, size):
        pygame.init()
        self.game_board = Board(size)
        self.turn_count = 0
        self.SCREEN_WIDTH = int((size)*50)
        self.SCREEN_HEIGHT = int((size)*50)
        self.BLACK = (0,0,0)
        self.all_sprite_list = pygame.sprite.Group()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.size = size

        #player instance
        self.players = []
        colors = ['red', 'blue', 'yellow', 'green']
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        for i in range(num_players):
            goal = get_goal(i)
            self.players.append(Player(colors[i], xpos[i], ypos[i], goal))
            self.game_board.board[ypos[i]][xpos[i]].element = self.players[i] 
            self.all_sprite_list = pygame.sprite.Group()
        
        #first draw screen
        self.draw_screen()

    def get_goal(self, i):
        goal = []
        if i == 0:
            for j in range(self.size):
                goal.append([self.size][i])
        elif i == 1:
            for j in range(self.size):
                goal.append([0][i])
        elif i == 2:
            for j in range(self.size):
                goal.append([i][self.size])
        elif i == 3:
            for j in range(self.size):
                goal.append([i][0])
        return goal
        
    def draw_screen(self):
        self.screen.fill([255, 255, 255])
        for x in range(50,self.SCREEN_WIDTH,50):
            pygame.draw.line(self.screen,self.BLACK, (x,0),(x,self.SCREEN_WIDTH), 2)
        for y in range(50,self.SCREEN_HEIGHT,50):
            pygame.draw.line(self.screen,self.BLACK, (0,y),(self.SCREEN_HEIGHT,y), 2)
        self.print_player()
        self.all_sprite_list.draw(self.screen)
        pygame.display.flip()


    def print_player(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*50
            self.players[i].rect.y = (self.players[i].ypos)*50
            self.all_sprite_list.add(self.players[i])


    def nextTurn(self):
        player = self.players[self.turn_count%4]
        
        player.move()
        self.draw_screen()
        self.turn_count +=1
        

#DFS
def DFS(tile_ori, tile_dest, visited_order):
    tile_ori.visited = True
    tile_ori.visited_order = visited_order
    if tile_dest.visited == True:
        return
    for i in tile_ori.neighbours: 
        if i.visited == False: 
            DFS(i, tile_dest, visited_order+1)

def find_shortest_path(tile):
    tile.is_shortest_path = True
    if tile.visited_order == 0:
        return tile
    
    posible_targets = []
    
    minimum = min(i.visited_order for i in tile.neighbours if i.visited)
    for i in tile.neighbours:
        if i.visited_order == minimum:
            posible_targets.append(i) 

    if len(posible_targets) == 1:
        neighbor_target = posible_targets[0]
    else:
        neighbors_minimum = []
        for i in posible_targets:
            neighbor_minimum = min(i.visited_order for i in tile.neighbours if i.visited)
            neighbors_minimum.append(neighbor_minimum)

        minimum = min(i for i in neighbors_minimum)
        for i in tile.neighbours:
            if i.visited_order == minimum:
                neighbor_target = i

    find_shortest_path(neighbor_target)


def call_DFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_ori = board_util[pos_ori[0]][pos_ori[1]]
    tiles_dest = board_util[pos_dest[0]][pos_dest[1]]
    DFS(tile_ori, tile_dest, 0)
    find_shortest_path(tile_dest)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_path(board_util)
    game.game_board.reset_tiles(board_util)


def BFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_ori = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    queque = []
    order = 0
    queque.append(tile_ori)

    tile_ori.visited = True
    while True:
        tile_ori = queque.pop(0)
        tile_ori.visited = True
        tile_ori.visited_order = order
        order += 1
        if tile_ori == tile_dest:
            break
        for i in tile_ori.neighbours:
            if queque.count(i) == 0 and i.visited == False:
                queque.append(i)
    
    find_shortest_path(tile_dest)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_path(board_util)
    game.game_board.reset_tiles(board_util)


def measure_time(sorting_alg, v):
  start = time.time()
  n = len(v)
  sorting_alg(v)
  end = time.time()
  return end-start

def main():
    game = Game(4, 9)
    
    # pos_ori = [1,1]
    # pos_dest = [3,3]
    
    # start = time.time()
    # BFS(game, pos_ori, pos_dest)
    # end = time.time()
    # print(end-start)

    # start = time.time()
    # call_DFS(game, pos_ori, pos_dest)
    # end = time.time()
    # print(end-start)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                game.nextTurn()

    pygame.quit()



if __name__== "__main__":
    main()


