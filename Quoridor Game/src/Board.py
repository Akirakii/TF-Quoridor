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
        self.removing_corner_walls()

    def indexing_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                if j+1 < self.size:
                    self.board[i][j].neighbors.append(self.board[i][j+1])
                if j-1 >= 0:
                    self.board[i][j].neighbors.append(self.board[i][j-1])
                if i-1 >= 0:
                    self.board[i][j].neighbors.append(self.board[i-1][j])
                if i+1 < self.size:
                    self.board[i][j].neighbors.append(self.board[i+1][j])
    
    def removing_corner_walls(self):
        for i in range(self.size):
            self.board[self.size-1][i].left_wall = None
            self.board[i][self.size-1].down_wall = None

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
                self.board[i][j].weight = 1

    def is_colliding(self, route, obstacles, pos, goal):
        x, y = pos[0], pos[1]

        for i in obstacles:
            if i.xpos == x and i.ypos == y:
                return True
        
        for i in goal:
            if i.xpos == x and i.ypos == y:
                return False

        route[y][x] = False
        for i in self.board[y][x].neighbors:
            if route[i.ypos][i.xpos]:
                is_colliding = self.is_colliding(route, obstacles, [i.xpos, i.ypos], goal)
        route[y][x] = True
        
        return is_colliding
