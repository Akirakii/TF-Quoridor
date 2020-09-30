import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, xpos, ypos, goal):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.goal = goal
        self.route = None
        super().__init__()
        self.image = pygame.image.load(color).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def move(self):
        self.route[self.ypos][self.xpos] = False
        if self.route[self.ypos][self.xpos+1]:
            self.xpos += 1 
        elif self.route[self.ypos][self.xpos-1]:
            self.xpos -= 1
        elif self.route[self.ypos-1][self.xpos]:
            self.ypos -= 1 
        elif self.route[self.ypos+1][self.xpos]:
            self.ypos += 1 

        self.route[self.ypos][self.xpos] = False

        print(self.ypos, self.xpos)
        for i in self.goal:
            print(i.ypos, i.xpos)
            if self.ypos == i.ypos and self.xpos == i.xpos:
                return True
        return False
