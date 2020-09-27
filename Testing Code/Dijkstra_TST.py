import networkx as nx


def dijsktra(Grafo, Nodos):
    # nx.to_dict_of_lists-> va devolver en un diccionario su lista de adyacencia
    grafo = nx.to_dict_of_lists(Grafo)
    # Creamos la la Lista "S" donde se almacenara el camino de vertices de costo minimo
    # Tambien la Cola "Queue" para la maxima prioridad del vertice con la distancia mas corta
    S = []
    Queue = []
    # Iniciamos en 0 hasta la cantidad de aristas todas las distancias "distancia" y
    # el sitio de donde vinieron "anterior"
    anterior = [0 for i in range(max(grafo) + 1)]
    distancia = [0 for i in range(max(grafo) + 1)]

    # Por cada nodo en el grafo-> ponerle valor infinito e insertarlo si es asi
    # a la cola de prioridad
    for nodo in grafo:
        distancia[nodo] = float("inf")
        Queue.append(nodo)
    # La distancia del primer nodo o source siempre sera 0 porque no llega de ningun lado
    distancia[Nodos[0]] = 0

    # Por cada valor en la cola
    while len(Queue) != 0:

        distancia_minima = float("inf")
        for i in Queue:
            if distancia[i] < distancia_minima:
                distancia_minima = distancia[i]
                nodo_temporal = i
        nodo_distancia_minima = nodo_temporal
        Queue.remove(nodo_distancia_minima)

        for vecino in grafo[nodo_distancia_minima]:
            if distancia[nodo_distancia_minima] == float("inf"):
                distancia_temporal = 0
            else:
                distancia_temporal = distancia[nodo_distancia_minima]
            distancia_con_peso = distancia_temporal + Grafo[nodo_distancia_minima][vecino]['peso']
            if distancia_con_peso < distancia[vecino]:
                distancia[vecino] = distancia_con_peso
                anterior[vecino] = nodo_distancia_minima

        if nodo_distancia_minima == Nodos[1]:
            if anterior[nodo_distancia_minima] != 0 or nodo_distancia_minima == Nodos[0]:
                while nodo_distancia_minima != 0:
                    S.insert(0, nodo_distancia_minima)
                    nodo_distancia_minima = anterior[nodo_distancia_minima]
                return S, 'Costo', len(S) - 1, 'numero de recorridos'


G = nx.Graph()
edges = [(1, 2), (1, 4), (2, 1), (2, 3), (2, 5), (3, 2), (3, 6), (4, 1), (4, 5), (4, 7), (5, 2), (5, 4), (5, 6), (5, 8),
         (6, 3), (6, 5), (6, 9), (7, 4), (7, 8), (8, 5), (8, 7), (8, 9), (9, 6), (9, 8)]
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
G.add_edges_from(edges)
for i, edge in enumerate(edges):
    G[edge[0]][edge[1]]['peso'] = weights[i]

print("La el recorrido minimo de 1 a 8  es ->", dijsktra(G, (1, 8)))

nx.draw(G, with_labels=True)
