import pygame
import Board
import Player

class Game():
    def __init__(self, num_players, size):
        pygame.init()
        self.game_board = Board.Board(size)
        self.turn_count = 0
        self.SCREEN_WIDTH = int((size)*50)
        self.SCREEN_HEIGHT = int((size)*50)
        self.BLACK = (0,0,0)
        self.all_sprite_list = pygame.sprite.Group()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.background = pygame.image.load("Quoridor Game/src/assets/board.png").convert()
        self.size = size

        #player instance
        self.players = []
        colors = ['Quoridor Game/src/assets/red.png', 'Quoridor Game/src/assets/blue.png', 'Quoridor Game/src/assets/yellow.png', 'Quoridor Game/src/assets/green.png']
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        for i in range(num_players):
            goal = self.get_goal(i)
            self.players.append(Player.Player(colors[i], xpos[i], ypos[i], goal))
            self.game_board.board[ypos[i]][xpos[i]].element = self.players[i] 
            self.all_sprite_list = pygame.sprite.Group()
        
        #first draw screen
        self.draw_screen()

    def get_goal(self, i):
        board_util = self.game_board.board
        goal = []
        if i == 0:
            for j in range(self.size):
                goal.append(board_util[self.size-1][j])
        elif i == 1:
            for j in range(self.size):
                goal.append(board_util[0][j])
        elif i == 2:
            for j in range(self.size):
                goal.append(board_util[j][self.size-1])
        elif i == 3:
            for j in range(self.size):
                goal.append(board_util[j][0])
        return goal
        

    def draw_screen(self):
        self.screen.blit(self.background, [0, 0])
        for x in range(50,self.SCREEN_WIDTH,50):
            pygame.draw.line(self.screen,self.BLACK, (x,0),(x,self.SCREEN_WIDTH), 2)
        for y in range(50,self.SCREEN_HEIGHT,50):
            pygame.draw.line(self.screen,self.BLACK, (0,y),(self.SCREEN_HEIGHT,y), 2)
        self.print_player()
        self.all_sprite_list.draw(self.screen)
        pygame.display.flip()


    def print_player(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*50
            self.players[i].rect.y = (self.players[i].ypos)*50
            self.all_sprite_list.add(self.players[i])


    def nextTurn(self):
        player = self.players[self.turn_count%4]

        #call_DFS(self, [game.players[1].ypos, game.players[1].xpos], game.players[1].goal)

        player.move()
        self.draw_screen()
        self.turn_count +=1