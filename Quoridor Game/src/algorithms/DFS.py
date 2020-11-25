import algorithms.Find_shortest_path as FSP

def DFS(tile, goal, visited_order):
    #tile: es la posicion inicial
    #goal: Meta para el jugador o IA
    #visited_order: Orden del cual ha sido visitado Orden del cual ha sido visitado
    tile.visited = True #se marca como visitado los nodos que van siendo llamados
    tile.visited_order = visited_order #se le asigna el orden de visita al nodo
    for i in goal: #Se recorre el array donde se almcenan las metas de los jugadores
        if i.visited == True: # se verifica si algun nodo dentro de goals ya fue visitado
            return tile
    for i in tile.neighbors: #se recorren todos los vecinos de tile
        if i is not None and i.visited == False: 
            last_tile = DFS(i, goal, visited_order+1)# Entonces en ese nodo hacer un nuevo DFS
            if last_tile is not None:
                return last_tile
    return None

def call_DFS(board, pos_ori, goal, obstacles):
    # board: es la matriz en donde se ubican todos los nodos que representan el tablero
    # pos_ori: Posición inicial del jugador o IA. array de posicion [x, y]
    # goal: Meta para el jugador o IA
    tile_ori = board[pos_ori[0]][pos_ori[1]] #inicia al jugador en la posicion [0][1]
    
    last_tile = DFS(tile_ori, goal, 0)
    if last_tile is None:
        return None

    shortest_path = [[False for i in range(len(board))] for j in range(len(board))]
    shortest_path.append(0) #colocamos en la ultima fila la distancia del camino
    FSP.find_shortest_path(last_tile, shortest_path, obstacles)
    return shortest_path