import algorithms.Find_shortest_path as FSP

def dijsktra(game, pos_ori, goal, obstacles):
    tile = board[pos_ori[0]][pos_ori[1]]

    tile_obstacles = []
    for i in obstacles:
        tile_obstacles.append(board_util[i.ypos][i.xpos])

    weightF=0
    queque = []
    order = 0
    queque.append(tile)
    while True:
        tile = queque.pop(0)
        tile.visited_order = order
        weightF=tile.weight
        order += 1
        tile.visited = True

        if tile in goal:
            break

        for i in tile.neighbours:
            if i.visited == False:
                i.weight=weightF+1
                i.previus=tile
                queque.append(i)
                i.visited = True

    tile.found=tile.weight

    while tile.previus!=None:
        tile.previus.found=tile.found-1
        tile=tile.previus

    shortest_path = [[False for i in range(len(board))] for j in range(len(board))]
    FSP.find_shortest_path(tile, shortest_path)
    return shortest_path