class Tile():
    def __init__(self, ypos, xpos):
        self.ypos = ypos # ypos: se guarda en que parte del tablero respecto a y se encuentra
        self.xpos = xpos # xpos: se guarda en que parte del tablero respecto a x se encuentra
        self.neighbours = [] # se almacenan los vecinos
        self.visited = False # se usa en los algoritmos de busqueda para saber si fue visitado o no
        self.visited_order = -1 # se usa para guardar el orden en que fue visitido en los algoritmos de busqueda
        self.weight = 1 # es el peso de la cola