import algorithms.Find_shortest_path as FSP

def DFS(tile, goal, visited_order, tile_obstacles):
    #tile: es la posicion inicial
    #goal: Meta para el jugador o IA
    #visited_order: Orden del cual ha sido visitado Orden del cual ha sido visitado
    #tile_obstacles: Cualquier jugador o IA excepto el mismo Cualquier jugador o IA excepto el mismo
    tile.visited = True #se marca como visitado los nodos que van siendo llamados
    tile.visited_order = visited_order #se le asigna el orden de visita al nodo
    for i in goal: #Se recorre el array donde se almcenan las metas de los jugadores
        if i.visited == True: # se verifica si algun nodo dentro de goals ya fue visitado
            return tile
    for i in tile.neighbors: #se recorren todos los vecinos de tile
        #Si el nodo no ha sido visitado y no tiene obstaculos
        if i.visited == False and i not in tile_obstacles: 
            last_tile = DFS(i, goal, visited_order+1, tile_obstacles)# Entonces en ese nodo hacer un nuevo DFS
            if last_tile is not None:
                return last_tile
    return None

def call_DFS(board, pos_ori, goal, obstacles):
    # board: es la matriz en donde se ubican todos los nodos que representan el tablero
    # pos_ori: Posición inicial del jugador o IA. array de posicion [x, y]
    # goal: Meta para el jugador o IA
    # obstacles: es una array que guarda a los otros jugadores

    tile_ori = board[pos_ori[0]][pos_ori[1]] #inicia al jugador en la posicion [0][1]
    
    tile_obstacles = []

    #Para acada obstaculo
    for i in obstacles:
        tile_obstacles.append(board[i.ypos][i.xpos])#Agrega la posicion donde se encuentra el obstaculo
    
    last_tile = DFS(tile_ori, goal, 0, tile_obstacles)
    shortest_path = [[False for i in range(len(board))] for j in range(len(board))]
    FSP.find_shortest_path(last_tile, shortest_path)
    return shortest_path