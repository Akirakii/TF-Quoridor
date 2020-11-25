import Tile


class Board():
    def __init__(self, size):
        self.size = size
        self.prohibited_walls = []

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
                else:
                    self.board[i][j].neighbors.append(None)
                if j-1 >= 0:
                    self.board[i][j].neighbors.append(self.board[i][j-1])
                else:
                    self.board[i][j].neighbors.append(None)
                if i-1 >= 0:
                    self.board[i][j].neighbors.append(self.board[i-1][j])
                else:
                    self.board[i][j].neighbors.append(None)
                if i+1 < self.size:
                    self.board[i][j].neighbors.append(self.board[i+1][j])
                else:
                    self.board[i][j].neighbors.append(None)

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

    def place_right_wall(self, pos):
        tile = self.board[pos[1]][pos[0]]
        if tile.right_wall == True:
            return

        print("right_wall colocado en: ", pos)
        tile.right_wall = True
        tile.cache.append([tile.neighbors[0].xpos, tile.neighbors[0].ypos])
        tile.neighbors[0].cache.append([tile.xpos, tile.ypos])
        del tile.neighbors[0].neighbors[1]
        tile.neighbors[0].neighbors.insert(1, None)
        del tile.neighbors[0]
        tile.neighbors.insert(0, None)

    def place_down_wall(self, pos):
        tile = self.board[pos[1]][pos[0]]
        if tile.down_wall == True:
            return

        print("down_wall colocado en: ", pos)
        tile.down_wall = True
        tile.cache.append([tile.neighbors[3].xpos, tile.neighbors[3].ypos])
        tile.neighbors[3].cache.append([tile.xpos, tile.ypos])
        del tile.neighbors[3].neighbors[2]
        tile.neighbors[3].neighbors.insert(2, None)
        del tile.neighbors[3]
        tile.neighbors.insert(3, None)

    def place_walls_AI(self, player, pos):
        x, y = pos[0], pos[1]
        route = player.route
        tile = self.board[y][x]
        route[y][x] = False
        wall_pos = None
        for i, neighbor in enumerate(tile.neighbors):
            if neighbor is not None and route[neighbor.ypos][neighbor.xpos]:
                if i == 0 and [False, x, y] not in self.prohibited_walls:
                    self.place_right_wall([x, y])
                    wall_pos = [False, x, y]
                elif i == 1 and [False, neighbor.xpos, neighbor.ypos] not in self.prohibited_walls:
                    self.place_right_wall([neighbor.xpos, neighbor.ypos])
                    wall_pos = [False, neighbor.xpos, neighbor.ypos]
                elif i == 2 and [True, neighbor.xpos, neighbor.ypos] not in self.prohibited_walls:
                    self.place_down_wall([neighbor.xpos, neighbor.ypos])
                    wall_pos = [True, neighbor.xpos, neighbor.ypos]
                elif i == 3 and [True, x, y] not in self.prohibited_walls:
                    self.place_down_wall([x, y])
                    wall_pos = [True, x, y]
                else:
                    wall_pos = self.place_walls_AI(player, [neighbor.xpos, neighbor.ypos])
        route[y][x] = True
        return wall_pos

    def rollback_last_wall(self, wall_pos):
        if wall_pos[0] == False:
            tile = self.board[wall_pos[2]][wall_pos[1]]
            print("right_wall removido en: ", [wall_pos[1], wall_pos[2]])

            tile.right_wall = False
            tile.cache.pop()
            del tile.neighbors[0]
            tile.neighbors.insert(0, self.board[tile.ypos][tile.xpos+1])
            tile.neighbors[0].cache.pop()
            del tile.neighbors[0].neighbors[1]
            tile.neighbors[0].neighbors.insert(1, tile)
        else:
            tile = self.board[wall_pos[2]][wall_pos[1]]
            print("down_wall removido en: ", [wall_pos[1], wall_pos[2]])

            tile.down_wall = False
            tile.cache.pop()
            del tile.neighbors[3]
            tile.neighbors.insert(3, self.board[tile.ypos+1][tile.xpos])
            tile.neighbors[3].cache.pop()
            del tile.neighbors[3].neighbors[2]
            tile.neighbors[3].neighbors.insert(2, tile)

    def is_colliding(self, route, pos, goal):
        x, y = pos[0], pos[1]

        for i in goal:
            if i.xpos == x and i.ypos == y:
                return False

        for cache_pos in self.board[y][x].cache:
            if route[cache_pos[1]][cache_pos[0]]:
                return True

        route[y][x] = False
        for neighbor in self.board[y][x].neighbors:
            if neighbor is not None and route[neighbor.ypos][neighbor.xpos]:
                is_colliding = self.is_colliding(
                    route, [neighbor.xpos, neighbor.ypos], goal)

        route[y][x] = True

        return is_colliding
