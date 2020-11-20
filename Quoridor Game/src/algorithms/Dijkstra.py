import algorithms.Find_shortest_path as FSP


def dijkstra(board, pos_ori, goal, obstacles):
    # board: es la matriz en donde se ubican todos los nodos que representan el tablero
    # pos_ori: Posición inicial del jugador o IA. array de posicion [x, y]
    # goal: Meta para el jugador o IA
    # obstacles: es una array que guarda a los otros jugadores 

    # tile obstacles: aqui guardamos los nodos de los obstaculos
    tile_obstacles = [] # se crea un array para guardar los obstaculos
    for i in obstacles: 
        tile_obstacles.append(board[i.ypos][i.xpos]) #se van guardando los nodos de cada obstaculos

    tile = board[pos_ori[0]][pos_ori[1]] #tile: es un iterador que va pasando entre los nodos
    queue = [] # se usa para almacenar los vecinos de cada nodo 
    queue_last_weight = [] # se usa para almacenar el peso del anterior nodo de cada nodo
    order = 0 # order: inicializamos el orden de visita
    queue.append(tile)
    queue_last_weight.append(0)
    weight_ori = tile.weight # se le asigna el peso del primer nodo, para que el algoritmo de find_shortest_path lo busque
    tile.visited = True #se marca como visitado el primer nodo
    
    #Visita cada nodo hasta encontrar el destino
    while True:
        tile.visited = True
        tile = queue.pop(0)# saca un nodo de la cola y lo asigna a la variable tile
        last_weight = queue_last_weight.pop(0) #obtenemos el peso del nodo anterior
        tile.weight += last_weight # el peso se suma al anterior peso
        tile.visited_order = tile.weight # almacenamos el peso en la matriz de nodos visitados

        if tile in goal: # se verifica si el tile es el destino
            break # si se llego al destino se rompe el bucle
        #Para cada vecino del nodo 
        for i in tile.neighbors:
            
            #si el nodo no esta en la cola
            #y el nodo no ha sido visitado
            #y el nodo no es un obstaculo
            if queue.count(i) == 0 and i.visited == False and i not in tile_obstacles: 
                queue.append(i)#se agregan los vecinos del nodo a la cola 
                queue_last_weight.append(tile.weight) #se le agrega el peso del nodo para el siguiente nodo
    
    #Creamos una matrix con el tamaño del tablero para que nos represente el camino que va a tomar el jugador
    shortest_path = [[False for i in range(len(board))] for j in range(len(board))] #lo rellenamos de False por cada nodo
    FSP.find_shortest_path(tile, shortest_path, weight_ori) #nos retorna la matriz con el camino en True
    return shortest_path #regresanis el camino que tomara el jugadorqueue_last_weight.pop(0)
