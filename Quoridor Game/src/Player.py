import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, xpos, ypos, goal):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.goal = goal
        super().__init__()
        self.image = pygame.image.load(color).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def move(self, board):
        tile = board[self.ypos][self.xpos]
        for indx, i in enumerate(board[self.ypos][self.xpos].neighbours):
            if i.is_shortest_path == True:
                if indx == 0:
                    self.xpos += 1 
                elif indx == 1:
                    self.xpos -= 1 
                elif indx == 2:
                    self.ypos -= 1 
                elif indx == 3:
                    self.ypos += 1
        if board[self.xpos][self.ypos] in self.goal:
            return True
        return False
