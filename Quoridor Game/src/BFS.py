import Find_shortest_path as FSP
def BFS(board, pos_ori, goal):
    tile_ori = board[pos_ori[0]][pos_ori[1]]
    queque = []
    order = 0
    queque.append(tile_ori)

    tile_ori.visited = True
    while True:
        tile_ori = queque.pop(0)
        tile_ori.visited = True
        tile_ori.visited_order = order
        order += 1
        if tile_ori in goal:
            break
        for i in tile_ori.neighbours:
            if queque.count(i) == 0 and i.visited == False:
                queque.append(i)
    
    FSP.find_shortest_path(tile_ori)