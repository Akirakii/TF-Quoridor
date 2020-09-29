import Find_shortest_path as Fsp

def DFS(tile, goal, visited_order):
    tile.visited = True
    tile.visited_order = visited_order
    for i in goal:
        if i.visited == True:
            return tile
    for i in tile.neighbours: 
        if i.visited == False: 
            last_tile = DFS(i, goal, visited_order+1)
            if last_tile is not None:
                return last_tile
    return None

def call_DFS(game, pos_ori, goal):
    board_util = game.game_board.board
    tile_ori = board_util[pos_ori[0]][pos_ori[1]]
    last_tile = DFS(tile_ori, goal, 0)
    Fsp.find_shortest_path(last_tile)
    game.game_board.print_visited_tiles(board_util)
    game.game_board.print_path(board_util)
    game.game_board.reset_tiles(board_util)