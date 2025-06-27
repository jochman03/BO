import numpy as np

def DPA(G, a, s):
    # G - graf w formie listy sąsiedztwa
    # a(u, v) - funkcja określająca wagę krawędzi między dwoma wierzchołkami
    # s - wierzchołek początkowy
    suma = 0 # sumaryczna waga krawędzi
    Q = [] # zbiór wierzchołków nienależących do MST
    A = [] # zbiór krawędzi MST  przechowuje krawedzie jako krotki (wierzchołek, wierzchołek)
    alfa = {} # słownik przechowujący dane   wierzchołek -> jego poprzednik
    beta = {} # słownik przechowujący dane   wierzchołek -> waga krawędzi z MST
    for u, neighbours in G.items():    # dla każdego wierzchołka z grafu
        alfa[u] = 0    # jego poprzedni wierzchołek to 0 (inicjalizacja)
        beta[u] = np.inf # waga krawędzi do MST to nieskończoność (inicjalizacja)
        Q.append(u)  # Dodawanie wierzchołka do zbioru wierzchołków nienależących do MST
    beta[s] = 0    # Odległość początkowego wierzchołka od MST to 0
    Q.remove(s)   # Usuwanie początkowego wierzchołka z Q
    u_last = s    # Ostatnim sprawdzanym wierzchołkiem był początkowy
    while len(Q) != 0:  # Główna pętla dla wszystkich niesprawdzonych
        for u in Q:   # dla każdego wierzchołka w Q
            if u in G[u_last]:  # Jeśli sąsiaduje z ostatnio sprawdzanym wierzchołkiem
                if a(u, u_last) < beta[u]:   # jeśli waga ich krawędzi jest mniejsza niż wierzchołka z MST
                    alfa[u] = u_last  # Poprzednikiem tego wierzchołka był ostatnio sprawdzany
                    beta[u] = a(u, u_last)  # Odległość tego wierzchołka od MST to waga krawędzi aktualnie sprawdzanego z poprzednio
        arg_min = None # deklaracja arg_min potrzebna do wyszukania wierzchołka z najmniejszą betą
        min_beta = np.inf # skoro najmniejsza na początku jest inf to każda != inf będzie mniejsza
        for u in Q:  
            if beta[u] < min_beta: # jeśli beta aktualnego wierzchołka jest mniejsza od ostatnio sprawdzanej
                min_beta = beta[u]   # to aktualny ma mniejszą
                arg_min = u # zostanie wyznaczony jako potencjalny najmniejszy
        if arg_min == None: # Sprawdzenie czy arg_min == None, jeśli tak, to graf niespójny
            break  # przerywa poszukiwania
        u_last = arg_min  # znaleziono wierzchołek o najmniejszym beta
        Q.remove(u_last)  # usuwanie go z Q
        A.append((alfa[u_last], u_last))  # Dodawanie krotki reprezentującej krawędz do MST
        suma = suma + a(alfa[u_last], u_last)  # Dodanie wagi krawędzi do całościowej sumy
    return (A, suma)
