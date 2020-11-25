import pygame
import os
import Board
import Player
import algorithms.DFS as DFS
import algorithms.BFS as BFS
import algorithms.Dijkstra as Dijkstra
import time
from termcolor import colored


class Game():
    def __init__(self, num_players, size):
        self.num_players = num_players
        self.game_board = Board.Board(size)
        self.turn_count = 0
        self.size = size
        self.game_over = False
        self.players = []
        self.times = []
        self.players_target = []
        self.execution_time = 0
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
            self.players_target.append(self.players[-1])
            self.all_sprite_list = pygame.sprite.Group()

        # first draw_screen:
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


    def place_walls_click(self, pos):
        if pos[0]/50 < 0.1 or pos[0]/50 > self.size - 0.1 or pos[1]/50 < 0.1 or pos[1]/50 > self.size - 0.1:
            return

        if pos[0]/50 > round(pos[0]/50, 0) - 0.1 and pos[0]/50 < round(pos[0]/50, 0) + 0.1 and pos[1]/50 > int(pos[1]/50) + 0.05 and pos[1]/50 < int(pos[1]/50) + 0.95:
            print("right_wall colocado en: ", [int(round(pos[0]/50, 0))-1, int(pos[1]/50)])
            pygame.draw.rect(self.background, (0,0,0), [((round(pos[0]/50, 0) - 0.05)*50, int(pos[1]/50)*50), (0.1*50, 50)]) 
            self.draw_screen()
            self.game_board.place_right_wall([int(round(pos[0]/50, 0))-1, int(pos[1]/50)])

        if pos[1]/50 > round(pos[1]/50, 0) - 0.1 and pos[1]/50 < round(pos[1]/50, 0) + 0.1 and pos[0]/50 > int(pos[0]/50) + 0.05 and pos[0]/50 < int(pos[0]/50) + 0.95:
            print("down_wall colocado en: ", [int(pos[0]/50), int(round(pos[1]/50,0))-1])
            pygame.draw.rect(self.background, (0,0,0), [((int(pos[0]/50))*50, (round(pos[1]/50, 0) - 0.05)*50), (50, 0.1*50)]) 
            self.draw_screen()
            
            self.game_board.place_down_wall([int(pos[0]/50), int(round(pos[1]/50,0))-1])


    def draw_wall(self, pos):
        if pos[0] == False:
            pygame.draw.rect(self.background, (0,0,0), [((pos[1]+1 - 0.05)*50, pos[2]*50), (0.1*50, 50)]) 
            print(pos[1], pos[2])
            self.draw_screen()

        else:
            pygame.draw.rect(self.background, (0,0,0), [(pos[1]*50, (pos[2]+1 - 0.05)*50), (50, 0.1*50)])
            print(pos[1], pos[2])
            self.draw_screen()


    def get_player_target_by_minimum_rout(self):
        minimum = 10000000000
        for i in self.players_target:
            if i.route_lenght < minimum:
                minimum = i.route_lenght
        for i in self.players_target:
            if i.route_lenght == minimum:
                return i


    def get_player_by_minimum_rout(self):
        minimum = 10000000000
        for i in self.players:
            if i.route_lenght < minimum:
                minimum = i.route_lenght
        for i in self.players:
            if i.route_lenght == minimum:
                return i


    def place_walls(self, player, obstacles):
        if self.players_target == []:
            return
        wall_pos = self.game_board.place_walls_AI(player, [player.xpos, player.ypos]) #si no, colocara una pared en el jugador con el camino mas corto
        if wall_pos is None:
            self.players_target.remove(player)
            new_player = self.get_player_target_by_minimum_rout()
            return self.place_walls(new_player, obstacles)
        routes_aux = []
        for i in range(self.num_players): #se va a recalcular el camino de todos despues de colocar la pared
            self.game_board.reset_tiles()
            routes_aux.append(self.players[i].route)
            if self.execute_search_algorithms(i, obstacles): #si la pared bloquea el camino de un jugador, se eliminara la pared y saldra del bucle
                for j in range(i+1):
                    self.players[i].route = routes_aux.pop(0)
                self.game_board.prohibited_walls.append(wall_pos)
                self.game_board.rollback_last_wall(wall_pos)
                return self.place_walls(player, obstacles)
        self.draw_wall(wall_pos)


    def execute_search_algorithms(self, player_num, obstacles):
        self.game_board.reset_tiles()
        board_util = self.game_board.board
        player = self.players[player_num]
        start = time.time()
        # Ejecutamos los algoritmos de busqueda cada vez que se detecta una colision o en el primer turno del jugador.
        # Los algoritmos de busqueda nos retorna la matriz con el camino de la solucion
        if self.turn_count < self.num_players or self.game_board.is_colliding(player.route, [player.xpos, player.ypos], player.goal):
            start = time.time()
            if player_num == 0:  # "red" El primer jugador ejecuta DFS 
                player.route = Dijkstra.dijkstra(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if player_num == 1:  # "blue" El segundo jugador ejecuta BFS
                player.route = DFS.call_DFS(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if player_num == 2:  # "yellow" El tercer jugador ejecuta Dijkstra
                player.route = BFS.BFS(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            if player_num == 3:  # "green" El cuarto jugador ejecuta Dijkstra
                player.route = Dijkstra.dijkstra(
                    board_util, [player.ypos, player.xpos], player.goal, obstacles)
            
            if player.route is None: # si no encuentra un camino, eliminara la ultima pared
                return True

            # print(colored(f"====================={player.name}, orden de visita=====================", 'yellow'))
            # self.game_board.print_visited_tiles()
            # print(colored(f"-----------------{player.name}, ruta-----------------", 'yellow'))
            # self.game_board.print_path(player.route)

            player.route_lenght = player.route[len(player.route)-1] #se asigna la distancia de la ruta del jugador a su variable
            del player.route[len(player.route)-1] #se elimina el valor distancia de la matriz ruta

        end = time.time()
        if player.save_time: 
            self.times[player_num].append(end-start)
            #print(colored(f"El tiempo de ejecucion de {player.name} es:  {end-start} ", 'green'))
            if end-start != 0.0:
                self.players[player_num].save_time = False

        return False # si encuentra un camino, no eliminara la ultima pared


    def next_turn(self):
        player = self.players[self.turn_count % self.num_players]
        #print(colored(f"/////////////////////////turno {self.turn_count} del jugador {player.name}/////////////////////////", 'red'))

        obstacles = []
        # each player is an obstacle
        for i in self.players:
            if i != player:
                obstacles.append(self.game_board.board[i.ypos][i.xpos])

        for i in range(self.num_players):
            self.players[i].save_time = True
            self.execute_search_algorithms(i, obstacles)

        
        if self.players_target != []:
            minimum_player = self.get_player_by_minimum_rout()
            if player == minimum_player: #si la ruta del jugador es la mas corta a comparacion de otros jugadores:
                self.game_over = player.move(self.game_board.board, obstacles) #el jugador se movera por la matriz solucion y retornara True si llega a la meta
            else:
                self.place_walls(self.get_player_target_by_minimum_rout(), obstacles)
        else:
            self.game_over = player.move(self.game_board.board, obstacles)

        for i in range(self.num_players):
            self.players[i].save_time = False

        self.draw_screen()

        if self.game_over:
            self.game_over_print(player)

        self.turn_count += 1
        return False
