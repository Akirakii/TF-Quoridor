import math
import pygame
import time



class Tile():
    def __init__(self):
        self.neighbors = []
        self.visited = False
        self.visited_order = -1
        self.is_shortest_path = False
        element = None
        self.peso=0
        self.previus=None
        self.encontrado=0
class Board():
    def __init__(self, size):
        self.board = [[Tile() for r in range(size)] for c in range(size)]
        self.indexing_tiles(self.board)

    def indexing_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j + 1 < len(board[i]):
                    board[i][j].neighbors.append(board[i][j + 1])

                if j - 1 >= 0:
                    board[i][j].neighbors.append(board[i][j - 1])
                if i - 1 >= 0:
                    board[i][j].neighbors.append(board[i - 1][j])
                if i + 1 < len(board):
                    board[i][j].neighbors.append(board[i + 1][j])

    def print_visited_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j].peso

                print(v, end=",  " if v in range(0, 9) else ", ")
            print("\n")

    def print_finding_path(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j].encontrado

                print(v, end=",  " if v in range(0, 9) else ", ")
            print("\n")

    def print_path(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(1 if board[i][j].is_shortest_path else 0, end=",  ")
            print("\n")

    def reset_tiles(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j].visited = False
                board[i][j].visited_order = -1
                board[i][j].is_shortest_path = False


class Player(pygame.sprite.Sprite):
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        super().__init__()
        self.image = pygame.image.load(color).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

class Game():
    def __init__(self, num_players, size):
        self.players = []
        colors = ['Quoridor Game/src/assets/red.png', 'Quoridor Game/src/assets/blue.png', 'Quoridor Game/src/assets/yellow.png', 'Quoridor Game/src/assets/green.png']
        xpos = [int(size / 2), int(size / 2), 0, size - 1]
        ypos = [0, size - 1, int(size / 2), int(size / 2)]
        self.game_board = Board(size)

        for i in range(num_players):
            self.players.append(Player(colors[i], xpos[i], ypos[i]))
            self.game_board.board[ypos[i]][xpos[i]].element = self.players[i]
        self.all_sprite_list = pygame.sprite.Group()

    def printPlayer(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos) * 50
            self.players[i].rect.y = (self.players[i].ypos) * 50
            self.all_sprite_list.add(self.players[i])


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


# DFS
def DFS(tile_ori, tile_dest, visited_order):
    tile_ori.visited = True
    tile_ori.visited_order = visited_order
    if tile_dest.visited == True:
        return
    for i in tile_ori.neighbors:
        if i.visited == False:
            DFS(i, tile_dest, visited_order + 1)


def call_DFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    DFS(tile_org, tile_dest, 0)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.set_all_visited_false(board_util)


def dijsktra(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_org = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]

    pesoF=0
    queque = []
    orden = 0
    queque.append(tile_org)
    while tile_org != tile_dest:

        tile_org = queque.pop(0)
        tile_org.visited_order = orden
        pesoF=tile_org.peso
        orden += 1
        tile_org.visited = True
        for i in tile_org.neighbors:

            if i.visited == False:
                i.peso=pesoF+1
                i.previus=tile_org
                queque.append(i)
                i.visited = True

    tile_org.encontrado=tile_org.peso

    while tile_org.previus!=None:

        tile_org.previus.encontrado=tile_org.encontrado-1
        tile_org=tile_org.previus
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_finding_path(board_util)
    game.game_board.set_all_visited_false(board_util)


def measure_time(sorting_alg, v):
    start = time.time()
    n = len(v)
    sorting_alg(v)
    end = time.time()
    return end - start


def main():
    pygame.init()
    done = False
    n = 9
    numPlayer = 4
    SCREEN_WIDTH = int((n) * 50)
    SCREEN_HEIGHT = int((n) * 50)
    BLACK = (0, 0, 0)
    all_sprite_list = pygame.sprite.Group()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    game = Game(numPlayer, n)
    pos_ori = [1, 1]
    pos_dest = [3, 3]
    start = time.time()
    dijsktra(game, pos_ori, pos_dest)
    end = time.time()
    print(end - start)

    start = time.time()
    call_DFS(game, pos_ori, pos_dest)
    end = time.time()
    print(end - start)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill([255, 255, 255])
        for x in range(50, SCREEN_WIDTH, 50):
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_WIDTH), 2)
        for y in range(50, SCREEN_HEIGHT, 50):
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_HEIGHT, y), 2)

        game.printPlayer()
        game.all_sprite_list.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

# DFS -- Akira


# BFS -- Cledmir
#Dijkstra -- Diego G
