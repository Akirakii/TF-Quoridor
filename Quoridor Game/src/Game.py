import pygame
import Board
import Player
import algorithms.DFS as DFS
import algorithms.BFS as BFS

class Game():
    def __init__(self, num_players, size):
        pygame.init()
        self.num_players = num_players
        self.game_board = Board.Board(size)
        self.turn_count = 0
        self.SCREEN_WIDTH = int((size)*50)
        self.SCREEN_HEIGHT = int((size)*50)
        self.BLACK = (0,0,0)
        self.all_sprite_list = pygame.sprite.Group()
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.background = pygame.image.load("Quoridor Game/src/assets/board.png")
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.Game_Over_background = pygame.image.load("Quoridor Game/src/assets/gameover.png")
        self.Game_Over_background = pygame.transform.scale(self.Game_Over_background, (self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.size = size
        self.game_over = False

        #player instance
        self.players = []
        colors = ['Quoridor Game/src/assets/red.png', 'Quoridor Game/src/assets/blue.png', 'Quoridor Game/src/assets/yellow.png', 'Quoridor Game/src/assets/green.png']
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        for i in range(num_players):
            goal = self.get_goal(i)
            self.players.append(Player.Player(colors[i], xpos[i], ypos[i], goal))
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
        if self.game_over == False:
            self.screen.blit(self.background, [0, 0])
            for x in range(50,self.SCREEN_WIDTH,50):
                pygame.draw.line(self.screen,self.BLACK, (x,0),(x,self.SCREEN_WIDTH), 2)
            for y in range(50,self.SCREEN_HEIGHT,50):
                pygame.draw.line(self.screen,self.BLACK, (0,y),(self.SCREEN_HEIGHT,y), 2)
            self.print_player()
            self.all_sprite_list.draw(self.screen)
            pygame.display.flip()

    def game_over_print(self,player):
        self.screen.blit(self.Game_Over_background, [0, 0])
        font = pygame.font.SysFont("serif", 25)
        posPng= player.color.find(".png")
        text = font.render("El jugador " + player.color[25:posPng] + " a ganado", True , self.BLACK)
        self.screen.blit(text, (self.SCREEN_WIDTH/5,self.SCREEN_HEIGHT-(self.SCREEN_HEIGHT/5)))
        pygame.display.flip() 


    def print_player(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*50
            self.players[i].rect.y = (self.players[i].ypos)*50
            self.all_sprite_list.add(self.players[i])


    def next_turn(self):
        board_util = self.game_board.board
        player = self.players[self.turn_count%self.num_players]

        obstacles = []
        #each player is an obstacle
        for i in self.players:
            if i != player:
                obstacles.append(i)

        if self.turn_count < self.num_players or self.game_board.is_colliding(player.route, obstacles, [player.xpos, player.ypos], player.goal):
            player.route = BFS.BFS(board_util, [player.ypos, player.xpos], player.goal, obstacles)
            print("\n\n///////////////////////////////////")
            self.game_board.print_visited_tiles()

        game_over = player.move()

        #debug board 
        print(player.color, "----------------------------------\n")
        self.game_board.print_path(player.route)
        self.game_board.reset_tiles()
        self.draw_screen()

        if game_over:
            self.game_over_print(player)

        self.turn_count +=1
        return False