import Tile

class Board():
    def __init__(self, size):
        self.size = size
        board = []
        for y in range(size):
            board.append([])
            for x in range(size):
                board[y].append(Tile.Tile(y, x))

        self.board = board
        self.indexing_tiles()

    def indexing_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                if j+1 < self.size:
                    self.board[i][j].neighbours.append(self.board[i][j+1])
                if j-1 >= 0:
                    self.board[i][j].neighbours.append(self.board[i][j-1])
                if i-1 >= 0:
                    self.board[i][j].neighbours.append(self.board[i-1][j])
                if i+1 < self.size:
                    self.board[i][j].neighbours.append(self.board[i+1][j])

    def print_visited_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                v = self.board[i][j].visited_order
                print(v, end = ",  " if v in range(0,9) else ", ")
            print("\n")
    
    def print_path(self, route):
        for i in range(self.size):
            for j in range(self.size):
                print(1 if route[i][j] else 0, end = ",  ")
            print("\n")

    def reset_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].visited = False
                self.board[i][j].visited_order = -1


    def is_colliding(self, route, tile_obstacles, pos, goal):
        x, y = pos[0], pos[1]

        for i in range(len(tile_obstacles)):
            if i.xpos == x and i.ypos == y:
                return True
        
        for i in goal:
            if y == i.ypos and x == i.xpos:
                return False

        route[y][x] = False
        if route[y][x+1]:
            self.is_colliding(route, tile_obstacles, [x+1, y], goal)
        elif route[y][x-1]:
            self.is_colliding(route, tile_obstacles, [x-1, y], goal)
        elif route[y-1][x]:
            self.is_colliding(route, tile_obstacles, [x, y-1], goal)
        elif route[y+1][x]:
            self.is_colliding(route, tile_obstacles, [x, y+1], goal)
        route[y][x] = True