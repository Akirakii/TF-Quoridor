class Tile():
    def __init__(self, ypos, xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.neighbours = []
        self.visited = False
        self.visited_order = -1
        self.is_shortest_path = False
        element = None