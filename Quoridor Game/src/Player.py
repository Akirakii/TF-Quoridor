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
        for i in board[self.ypos][self.xpos].neighbours:
            if i.is_shortest_path == True:
                if self.xpos < i.xpos:
                    self.xpos += 1 
                elif self.xpos > i.xpos:
                    self.xpos -= 1 
                elif self.ypos > i.ypos:
                    self.ypos -= 1 
                elif self.ypos < i.ypos:
                    self.ypos += 1
        if board[self.xpos][self.ypos] in self.goal:
            return True
        return False
