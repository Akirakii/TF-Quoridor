import pygame

class Player(pygame.sprite.Sprite):
    #color: se le asigna un color a cada jugador
    #xpos: se define en que posicion respecto a x esta el jugaodor
    #ypos: se define en que posicion respecto a y esta el jugaodor
    #goal: es la meta del jugador

    def __init__(self, color, xpos, ypos, goal):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.goal = goal
        self.route = None
        super().__init__() # se usa para poder imprimir el jugador
        self.image = pygame.image.load(color).convert() # se le asigna el sprite al jugador
        self.image.set_colorkey((0, 0, 0)) # se borra el fondo que se produce al moverse
        self.rect = self.image.get_rect() # se le asigna la forma de cuadrado para insertar la imagen
    
    def move(self): # se encarga de mover al jugador
        # se le pone el valor de falso a la ruta antes de moverse
        self.route[self.ypos][self.xpos] = False 
        # se verifica a que posicion se va a mover el jugador
        if self.xpos+1 < len(self.route) and self.route[self.ypos][self.xpos+1]: 
            self.xpos += 1 
        elif self.xpos-1 >= 0 and self.route[self.ypos][self.xpos-1]:
            self.xpos -= 1
        elif self.ypos-1 >= 0 and self.route[self.ypos-1][self.xpos]:
            self.ypos -= 1 
        elif self.ypos+1 < len(self.route) and self.route[self.ypos+1][self.xpos]:
            self.ypos += 1 

        self.route[self.ypos][self.xpos] = False # se le asigna falso a la ruta despues de moverse

        for i in self.goal: # se recorre los destinos de los jugadores
            if self.ypos == i.ypos and self.xpos == i.xpos:# se verifica si  el jugador esta en el la meta
                return True
        return False
