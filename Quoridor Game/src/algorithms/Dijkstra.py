import algorithms.Find_shortest_path as FSP

def dijkstra(board, pos_ori, goal, obstacles):
    tile_obstacles = []
    for i in obstacles:
        tile_obstacles.append(board[i.ypos][i.xpos])

    tile = board[pos_ori[0]][pos_ori[1]]
    queque = []
    queque.append(tile)
    weight = 0

    tile.visited = True
    while True:
        tile = queque.pop(0)
        tile.visited = True
        tile.visited_order = weight
        weight += tile.weight
        if tile in goal:
            break
        for i in tile.neighbours:
            if queque.count(i) == 0 and i.visited == False and i not in tile_obstacles:
                queque.append(i)

    shortest_path = [[False for i in range(len(board))] for j in range(len(board))]
    FSP.find_shortest_path(tile, shortest_path)
    return shortest_path