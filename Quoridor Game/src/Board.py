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
            self.board[self.size-1][i].righht_wall = None
            self.board[i][self.size-1].down_wall = None

    def print_visited_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                v = self.board[i][j].visited_order
                print(v, end=",  " if v in range(0, 9) else ", ")
            print("\n")

    def print_path(self, route):
        for i in range(self.size):
            for j in range(self.size):
                print(1 if route[i][j] else 0, end=",  ")
            print("\n")

    def reset_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].visited = False
                self.board[i][j].visited_order = -1
                self.board[i][j].weight = 1

    def is_colliding(self, route, obstacles, pos, goal):
        x, y = pos[0], pos[1]
        tile = self.board[y][x]

        for i in obstacles:
            if i.xpos == x and i.ypos == y:
                return True

        for i in goal:
            if i.xpos == x and i.ypos == y:
                return False

        if route[y][x]:
            # validando right_wall al lado derecho del jugador
            if tile.right_wall and tile.ypos == y and tile.xpos > x:
                return True
            # validando down_wall al lado inferior del jugador
            if tile.down_wall and tile.xpos == x and tile.ypos < y:
                return True

        route[y][x] = False
        for neighbor in tile.neighbors:
            if route[neighbor.ypos][neighbor.xpos]:
                # validando right_wall del vecino al lado izquierdo del jugador
                if neighbor.right_wall and neighbor.ypos == y and neighbor.xpos < x:
                    return True
                # validando down_wall del vecino al lado superior del jugador
                if neighbor.down_wall and neighbor.xpos == x and neighbor.ypos > y:
                    return True

                is_colliding = self.is_colliding(
                    route, obstacles, [neighbor.xpos, neighbor.ypos], goal)

        route[y][x] = True

        return is_colliding
