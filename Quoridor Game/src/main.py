import math
import pygame
import time
import Game
import BFS



def main():
    num_players = 1
    board_size = 21
    game = Game.Game(num_players, board_size)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if game.next_turn():
                    done = True

    pygame.quit()


if __name__== "__main__":
    main()
