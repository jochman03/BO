def bfs (G, s):
    # G - graf w formie listy sąsiedztwa
    # s - index wierzchołka początkowego
    No = {}         # słownik przechowujący wartości:   numer wierzchołka : kolejność przeszukiwania
    Nr = 1          # Numer wierzchołka
    No[s] = Nr      # wpisanie do słownika pierwszego wierzchołka z numerem 1
    queue_fifo = [] # definicja Kolejki FIFO
    is_cyclic = 0   # definicja zmiennej określającej czy graf jest cykliczny
    is_connected = 1  # definicja zmiennej określającej czy graf jest spójny
    parent = {s: None}  # definicja słownika przechowujacego wartość:  wierzchołek : jego rodzic

    for neighbour in G[s]:   
        queue_fifo.append(neighbour)      # dodanie sąsiadów do kolejki
        parent[neighbour] = s           # dodanie rodzica wierzchołka
    while len(queue_fifo) != 0:   # Dopóki kolejka nie jest pusta
        v = queue_fifo.pop(0)  # Pobranie pierwszego elementu z kolejki
        Nr = Nr + 1            # Inkrementacja numeru wierzchołka
        No[v] = Nr             # Dodanie wierzchołka do słownika
        for neighbour in G[v]:   
            if neighbour not in No:   # Jeśli sąsiedni wierzchołek nie znajduje się w głównym słowniku,
                queue_fifo.append(neighbour) #  to trzeba go dodać do kolejki
                parent[neighbour] = v   # dodanie rodzica wierzchołka
            elif parent[v] != neighbour:   # Jeśli sąsiedni wierzchołek jest w słowniku i nie jest rodzicem
                is_cyclic = 1   # to mamy do czynienia z cyklem

    if len(No) < len(G.keys()):     # Sprawdzenie czy graf jest spójny
        is_connected = 0     # jak słownik ma mniej elementów niż graf, to graf nie jest spójny
        
    # wypisanie wniosków
    print("Kolejność odwiedzania wierzchołków:", *No.keys())
    print("Graf", "Spójny" if is_connected == 1 else "Niespójny")
    print("Graf","Cykliczny" if is_cyclic == 1 else "Acykliczny")
    