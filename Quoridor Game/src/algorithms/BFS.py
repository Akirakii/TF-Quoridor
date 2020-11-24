import algorithms.Find_shortest_path as FSP


def BFS(board, pos_ori, goal, obstacles):
    # board: es la matriz en donde se ubican todos los nodos que representan el tablero
    # pos_ori: Posición inicial del jugador o IA. array de posicion [x, y]
    # goal: Meta para el jugador o IA
    # obstacles: es una array que guarda a los otros jugadores 

    # tile obstacles: aqui guardamos los nodos de los obstaculos
    tile_obstacles = [] # se crea un array para guardar los obstaculos
    for i in obstacles: 
        tile_obstacles.append(board[i.ypos][i.xpos]) #se van guardando los nodos de cada obstaculos

    tile = board[pos_ori[0]][pos_ori[1]] #tile: es un iterador que va pasando entre los nodos
    queque = [] # queue: se usa para almacenar los vecinos de cada nodo 
    order = 0 # order: inicializamos el orden de visita
    queque.append(tile)
    
    tile.visited = True #se marca como visitado el primer nodo
    
    #Visita cada nodo hasta encontrar el destino
    while True:
        if queque == []:
            return None

        tile = queque.pop(0)# saca un nodo de la cola y lo asigna a la variable tile
        tile.visited = True #se marca como visitado los nodos que van siendo llamados
        tile.visited_order = order #se le asigna el orden de visita al nodo
        order += 1

        if tile in goal: # se verifica si el tile es el destino
            break # si se llego al destino se rompe el bucle
        #Para cada vecino del nodo 
        for i in tile.neighbors:
            
            #si el nodo no esta en la cola
            #y el nodo no ha sido visitado
            #y el nodo no es un obstaculo
            if i is not None and queque.count(i) == 0 and i.visited == False and i not in tile_obstacles: 
                queque.append(i)#se agregan los vecinos del nodo a la cola 
    
    #Creamos una matrix con el tamaño del tablero para que nos represente el camino que va a tomar el jugador
    shortest_path = [[False for i in range(len(board))] for j in range(len(board))] #lo rellenamos de False por cada nodo
    shortest_path.append(0) #colocamos en la ultima fila la distancia del camino
    FSP.find_shortest_path(tile, shortest_path) #nos retorna la matriz con el camino en True
    return shortest_path #regresanis el camino que tomara el jugador