def find_shortest_path(tile):
    if tile.visited_order != 0:
        tile.is_shortest_path = True
    if tile.visited_order == 0:
        return tile
    
    posible_targets = []
    
    minimum = min(i.visited_order for i in tile.neighbours if i.visited)
    for i in tile.neighbours:
        if i.visited_order == minimum:
            posible_targets.append(i) 

    if len(posible_targets) == 1:
        neighbor_target = posible_targets[0]
    else:
        neighbors_minimum = []
        for i in posible_targets:
            neighbor_minimum = min(i.visited_order for i in tile.neighbours if i.visited)
            neighbors_minimum.append(neighbor_minimum)

        minimum = min(i for i in neighbors_minimum)
        for i in tile.neighbours:
            if i.visited_order == minimum:
                neighbor_target = i

    find_shortest_path(neighbor_target)