import pygame
import Board
import Player
import DFS
import BFS
import Find_shortest_path

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
        board_util = self.game_board.board
        player = self.players[self.turn_count%self.num_players]
        if player == self.players[0]:
            DFS.call_DFS(board_util, [player.ypos, player.xpos], player.goal)
        elif player == self.players[1]:
            BFS.BFS(board_util, [player.ypos, player.xpos], player.goal)
        #debug board 
        print("\n\n///////////////////////////////////")
        self.game_board.print_visited_tiles()
        print("----------------------------------\n")
        self.game_board.print_path()

        if player.move(board_util):
            print("Ganaste XD")
            return True
        
        #self.game_board.reset_tiles()
        self.draw_screen()
        self.turn_count +=1
        return False