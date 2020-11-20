def find_shortest_path(tile, shortest_path, weight_ori=-1):
    if tile.visited_order != 0: #mientras no llegue a su destino, va marcando True en el camino
        shortest_path[tile.ypos][tile.xpos] = True
    if tile.visited_order == 0 or tile.weight == weight_ori: #cuando encuentra la posicion del jugador, retorna 
        return
    
    posible_targets = [] #almacenamos todos los valores minimos repetidos aqui
    
    minimum = min(i.visited_order for i in tile.neighbors if i.visited)
    for i in tile.neighbors:
        if i.visited_order == minimum:
            posible_targets.append(i)  # almacenamos todos los valores minimos repetidos

    if len(posible_targets) == 1: # si no hay repetidos, se le asigna al vecino destino
        neighbor_target = posible_targets[0]
    else: # si hay elementos repetidos
        neighbors_minimum = []
        for i in posible_targets:
            neighbor_minimum = min(i.visited_order for i in tile.neighbors if i.visited) # se almacena el minimo de los vecinos del nodo candidato
            neighbors_minimum.append(neighbor_minimum) 

        minimum = min(i for i in neighbors_minimum) # se selcciona el candidato con el minimo de los valores minimos de los vecinos
        for i in tile.neighbors:
            if i.visited_order == minimum:
                neighbor_target = i

    find_shortest_path(neighbor_target, shortest_path, weight_ori) #se llama al vecino destino