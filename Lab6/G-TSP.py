import numpy as np

def G_TSP(graph, weights):
    sorted_edges = sorted(weights.items(), key=lambda item: item[1]) # sortowanie krawedzi po wagach
    Eo = dict() # Słownik:  wierzchołek początkowy -> wierzchołek końcowy krawędzi
    cost = 0 # koszt całkowity
    def is_cycle(u, v): # Funkcja sprawdzająca czy dodanie krawędzi (u, v) spowoduje podcykl
        node = v # wierzchołek końcowy
        goal = u # wierzchołek początkowy
        while node in Eo: # dopóki wierzchołek końcowy krawędzi jest w słowniku
            node = Eo[node] # wybieranie kolejnego wierzchołka z krawezi
            if node == goal: # jeśli istnieje inna ścieżka do docelowego wierzchołka
                return True # to znaczy, że dodanie krawędzi (u, v) spowoduje podcykl
        return False # W tym miejscu nie ma podcyklu
    
    for ((u, v), weight) in sorted_edges:   # dla każdej krawędzi (u, v) w posortowanej liście krawędzi
        if u in Eo.keys() or v in Eo.values(): # jeśli wierzchołek początkowy krawędzi jest już w słowniku 
            continue # lub wierzchołek końcowy krawędzi jest już w słowniku, to trzeba pominąć
        if len(Eo.keys()) < (len(graph.keys()) -1): # jeśli to ostatnia krawędź, to może być cykl
            if is_cycle(u, v): # sprawdzanie czy dodanie krawędzi (u, v) spowoduje podcykl
                continue # jeśli tak, to pomijanie krawędzi
        Eo[u] = v # dodawanie krawędzi (u, v) do słownika
        cost += weight # dodawanie wagi krawędzi do kosztu całkowitego
    path = list() # lista wierzchołków w ścieżce
    if len(Eo) < len(graph): # nie odwiedzono wszystkich wierzchołków
        return None, 0  # czyli nie rozwiązano problemu
    node = sorted_edges[0][0][0] # pierwszy wierzchołek z listy posortowanych krawedzi
    path.append(node) # dodawanie wierzchołka początkowego do listy wierzchołków w ścieżce
    while len(path) < len(Eo.keys()): # dopóki liczba wierzchołków w ścieżce jest mniejsza niż liczba krawędzi w słowniku
        if node not in Eo: # jeśli wierzchołek początkowy krawędzi nie jest w słowniku
            return None, 0 # To algorytm zawiódł
        path.append(Eo[node]) # dodawanie wierzchołka do wyznaczonej ścieżki
        node = Eo[node]  # wybieranie kolejnego wierzchołka na podstawie krawędzi
    return path, cost # zwracanie ścieżki i kosztu