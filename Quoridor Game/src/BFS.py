def BFS(game, pos_ori, pos_dest):
    board_util = game.game_board.board
    tile_ori = board_util[pos_ori[0]][pos_ori[1]]
    tile_dest = board_util[pos_dest[0]][pos_dest[1]]
    queque = []
    order = 0
    queque.append(tile_ori)

    tile_ori.visited = True
    while True:
        tile_ori = queque.pop(0)
        tile_ori.visited = True
        tile_ori.visited_order = order
        order += 1
        if tile_ori == tile_dest:
            break
        for i in tile_ori.neighbours:
            if queque.count(i) == 0 and i.visited == False:
                queque.append(i)
    
    find_shortest_path(tile_dest)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_path(board_util)
    game.game_board.reset_tiles(board_util)