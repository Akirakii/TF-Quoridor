import algorithms.Find_shortest_path as FSP

def DFS(tile, goal, visited_order, tile_obstacles):
    tile.visited = True
    tile.visited_order = visited_order
    for i in goal:
        if i.visited == True:
            return tile
    for i in tile.neighbours: 
        if i.visited == False and i not in tile_obstacles: 
            last_tile = DFS(i, goal, visited_order+1, tile_obstacles)
            if last_tile is not None:
                return last_tile
    return None

def call_DFS(board, pos_ori, goal, obstacles):
    tile_ori = board[pos_ori[0]][pos_ori[1]]

    tile_obstacles = []
    for i in obstacles:
        tile_obstacles.append(board[i.ypos][i.xpos])
    
    last_tile = DFS(tile_ori, goal, 0, tile_obstacles)
    shortest_path = [[False for i in range(len(board))] for j in range(len(board))]
    FSP.find_shortest_path(last_tile, shortest_path)
    return shortest_path
  
