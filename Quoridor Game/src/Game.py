import pygame
import os
import Board
import Player
import algorithms.DFS as DFS
import algorithms.BFS as BFS
import algorithms.Dijkstra as Dijkstra
import time


class Game():
    def __init__(self, num_players, size):
        self.num_players = num_players
        self.game_board = Board.Board(size)
        self.turn_count = 0
        self.size = size
        self.game_over = False
        self.players = []
        self.times = []
        for i in range(num_players):
            self.times.append([])

        # graphic settings
        pygame.init()
        # Where your .py file is located
        current_path = os.path.dirname(__file__)
        # The image folder path
        image_path = os.path.join(current_path, 'assets')
        self.SCREEN_WIDTH = int((size)*50)
        self.SCREEN_HEIGHT = int((size)*50)
        self.BLACK = (0, 0, 0)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_walls_list = []
        self.screen = pygame.display.set_mode(
            [self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.background = pygame.image.load(
            os.path.join(image_path, 'board.png'))
        self.background = pygame.transform.scale(
            self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.Game_Over_background = pygame.image.load(
            os.path.join(image_path, 'gameover.png'))
        self.Game_Over_background = pygame.transform.scale(
            self.Game_Over_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # player instance
        names = ['red', 'blue', 'yellow', 'green']
        images = [pygame.image.load(os.path.join(image_path, 'red.png')), pygame.image.load(os.path.join(image_path, 'blue.png')),
                  pygame.image.load(os.path.join(image_path, 'yellow.png')), pygame.image.load(os.path.join(image_path, 'green.png'))]
        xpos = [int(size/2), int(size/2), 0, size-1]
        ypos = [0, size-1, int(size/2), int(size/2)]
        for i in range(num_players):
            goal = self.get_goal(i)
            self.players.append(Player.Player(
                names[i], images[i], xpos[i], ypos[i], goal))
            self.all_sprite_list = pygame.sprite.Group()

        # first draw_screen()
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
            for x in range(50, self.SCREEN_WIDTH, 50):
                pygame.draw.line(self.screen, self.BLACK,
                                 (x, 0), (x, self.SCREEN_WIDTH), 2)
            for y in range(50, self.SCREEN_HEIGHT, 50):
                pygame.draw.line(self.screen, self.BLACK,
                                 (0, y), (self.SCREEN_HEIGHT, y), 2)
            self.print_player()
            self.all_sprite_list.draw(self.screen)
            print(len(self.all_walls_list))
            for i in self.all_walls_list:
                pygame.draw.rect(self.background, (255, 255, 255), i)
            pygame.display.flip()

    def game_over_print(self, player):
        self.screen.blit(self.Game_Over_background, [0, 0])
        font = pygame.font.SysFont("serif", 25)
        text = font.render("El jugador " + player.name +
                           " a ganado", True, self.BLACK)
        self.screen.blit(text, (self.SCREEN_WIDTH/5,
                                self.SCREEN_HEIGHT-(self.SCREEN_HEIGHT/5)))
        pygame.display.flip()

    def print_player(self):
        for i in range(len(self.players)):
            self.players[i].rect.x = (self.players[i].xpos)*50
            self.players[i].rect.y = (self.players[i].ypos)*50
            self.all_sprite_list.add(self.players[i])

    def place_walls(self, pos):
        if pos[0]/50 < 0.1 or pos[0]/50 > self.SCREEN_WIDTH - 0.1 or pos[1]/50 < 0.1 or pos[0]/50 > self.SCREEN_HEIGHT - 0.1:
            return

        if pos[0]/50 > round(pos[0]/50, 0) - 0.1 and pos[0]/50 < round(pos[0]/50, 0) + 0.1 and pos[1]/50 > int(pos[1]/50) + 0.05 and pos[1]/50 < int(pos[1]/50) + 0.95:
            print("right_wall colocado en: ", (round(pos[0]/50, 0) - 0.1, int(pos[1]/50) + 0.1), (round(pos[0]/50, 0) + 0.1, int(pos[1]/50) + 0.9))
            self.all_walls_list.append((((round(pos[0]/50, 0) - 0.1)*50, (int(pos[1]/50) + 0.1)*50), ((round(pos[0]/50, 0) + 0.1), (int(pos[1]/50) + 0.9)*10)))
            self.draw_screen()


        if pos[1]/50 > round(pos[1]/50, 0) - 0.1 and pos[1]/50 < round(pos[1]/50, 0) + 0.1 and pos[0]/50 > int(pos[0]/50) + 0.05 and pos[0]/50 < int(pos[0]/50) + 0.95:
            print("down_wall colocado en: ", ((int(pos[0]/50) + 0.05), round(pos[1]/50, 0) - 0.1), (int(pos[0]/50) + 0.95, round(pos[1]/50, 0) + 0.1))


    def next_turn(self):
        board_util = self.game_board.board
        player = self.players[self.turn_count % self.num_players]

        obstacles = []
        # each player is an obstacle
        for i in self.players:
            if i != player:
                obstacles.append(i)

        start = time.time()

        # Ejecutamos los algoritmos de busqueda cada vez que se detecta una colision o en el primer turno del jugador.
        # Los algoritmos de busqueda nos retorna la matriz con el camino de la solucion
        if self.turn_count < self.num_players or self.game_board.is_colliding(player.route, obstacles, [player.xpos, player.ypos], player.goal):
            if self.turn_count % self.num_players == 0:  # El primer jugador ejecuta DFS
                player.route = DFS.call_DFS(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if self.turn_count % self.num_players == 1:  # El segundo jugador ejecuta BFS
                player.route = BFS.BFS(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if self.turn_count % self.num_players == 2:  # El tercer jugador ejecuta Dijkstra
                player.route = Dijkstra.dijkstra(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if self.turn_count % self.num_players == 3:  # El cuarto jugador ejecuta Dijkstra
                player.route = Dijkstra.dijkstra(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            print("\n\n///////////////////////////////////")
            self.game_board.print_visited_tiles()

        # el jugador se movera por la matriz solucion y retornara True si llega a la meta
        self.game_over = player.move()
        end = time.time()
        print("El tiempo de ejecucion es: " + str(end-start))
        self.times[self.turn_count % self.num_players].append(end-start)

        print(player.name, "----------------------------------\n")
        self.game_board.print_path(player.route)
        self.game_board.reset_tiles()
        self.draw_screen()

        if self.game_over:
            self.game_over_print(player)

        self.turn_count += 1
        return False
