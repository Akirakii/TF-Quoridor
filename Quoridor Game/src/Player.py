import pygame

class Player(pygame.sprite.Sprite):
    #name: se le asigna un nombre a cada jugador
    #xpos: se define en que posicion respecto a x esta el jugaodor
    #ypos: se define en que posicion respecto a y esta el jugaodor
    #goal: es la meta del jugador

    def __init__(self, name, image, xpos, ypos, goal):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.goal = goal
        self.route = None
        self.route_lenght = 0
        super().__init__() # se usa para poder imprimir el jugador
        self.image = image # se le asigna el sprite al jugador
        self.image.set_colorkey((0, 0, 0)) # se borra el fondo que se produce al moverse
        self.rect = self.image.get_rect() # se le asigna la forma de cuadrado para insertar la imagen
    
    def move(self, board, obstacles): # se encarga de mover al jugador
        # se le pone el valor de falso a la ruta antes de moverse
        self.route[self.ypos][self.xpos] = False 
        # se verifica a que posicion se va a mover el jugador
        if self.xpos+1 < len(self.route) and self.route[self.ypos][self.xpos+1] and board[self.ypos][self.xpos].right_wall == False: 
            self.xpos += 1 
        elif self.xpos-1 >= 0 and self.route[self.ypos][self.xpos-1] and board[self.ypos][self.xpos-1].right_wall == False: 
            self.xpos -= 1 
        elif self.ypos-1 >= 0 and self.route[self.ypos-1][self.xpos] and board[self.ypos-1][self.xpos].down_wall == False:
            self.ypos -= 1 
        elif self.ypos+1 < len(self.route) and self.route[self.ypos+1][self.xpos] and board[self.ypos][self.xpos].down_wall == False:
            self.ypos += 1 

        self.route[self.ypos][self.xpos] = False # se le asigna falso a la ruta despues de moverse

        if board[self.ypos][self.xpos] in obstacles:
            self.move(board, obstacles)

        for i in self.goal: # se recorre los destinos de los jugadores
            if self.ypos == i.ypos and self.xpos == i.xpos:# se verifica si  el jugador esta en el la meta
                return True
        return False
