import sys
import pygame
import time
import Game
import matplotlib.pyplot as plt

def main():

    sys.setrecursionlimit(10**7)

    num_players = 3
    board_size = 15
    game = Game.Game(num_players, board_size)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and game.game_over == False:
                if game.next_turn():
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN and game.game_over == True:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                game.place_walls_click(pos)

    for i in range(len(game.times)):
        print("jugador " + str(i))
        for j in range(len(game.times[i])):
            print(game.times[i][j], end = ",  ")
        print("\n")
    
    for i in range(len(game.times)):
        turns = []
        for j in range(len(game.times[i])):
            turns.append(j)
        plt.plot(turns, game.times[i])   

    plt.xlabel('turns')
    plt.ylabel('time in sec')
    plt.title('time test')
    plt.legend(['DFS','BFS','Dijkstra'])
    plt.show()

    pygame.quit()


if __name__== "__main__":
    main()
