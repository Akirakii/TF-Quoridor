import sys
import pygame
import time
import Game

def main():
    sys.setrecursionlimit(10**7)

    num_players = 4
    board_size = 41
    game = Game.Game(num_players, board_size)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if game.game_over == False:
                if game.next_turn():
                    done = True
            # if event.type == pygame.KEYDOWN and game.game_over == False:
            #     if game.next_turn():
            #         done = True
            if event.type == pygame.MOUSEBUTTONDOWN and game.game_over == True:
                done = True

    for i in range(len(game.times)):
        print("jugador " + str(i))
        for j in range(len(game.times[i])):
            print(game.times[i][j], end = ",  ")
        print("\n")

    pygame.quit()


if __name__== "__main__":
    main()
