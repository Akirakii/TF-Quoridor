import sys
import pygame
import time
import Game
import matplotlib.pyplot as plt

def main():

    sys.setrecursionlimit(10**7)

    num_players = 3 # VALORES EDITABLES
    board_size = 21 # VALORES EDITABLES
    
    game = Game.Game(num_players, board_size)
    end_game = False
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and game.game_over == False:
                while game.game_over == False: # COMENTAR ESTO PARA QUE NO CORRTA EL JUEGO AUTOMATICAMENTE
                    if game.next_turn():
                        done = True
            if event.type == pygame.MOUSEBUTTONDOWN and game.game_over == True:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                game.place_walls_click(pos)


    # for i in range(len(game.times)):
    #     print("jugador " + str(i))
    #     for j in range(len(game.times[i])):
    #         print(game.times[i][j], end = ",  ")
    #     print("\n")
    
    print(len(game.times))
    print(len(game.times[0]))
    
    for i in range(len(game.times)):
        turns = []
        for j in range(len(game.times[i])):
            turns.append(j)
        plt.plot(turns, game.times[i])   

    plt.xlabel('turns')
    plt.ylabel('time in sec')
    plt.title(f'time test with {board_size}*{board_size}')
    plt.legend(['DFS','BFS','Dijkstra'])
    plt.show()

    pygame.quit()


if __name__== "__main__":
    main()
