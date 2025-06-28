import numpy as np
import math

def path(sp, u, s, p, Tz, price): # parametry -> sp - lista poprzedników, u - wierzchołek, s - wierzchołek początkowy
    # p - słownik - poprzedni wierzchołek: następny wierzchołek, Tz - zbiór wierzchołków odwiedzonychm, prize - koszt
    if u not in sp:  # jak wierzchołek nie należy do sp, to jest ostatni, trzeba dodać.
        sp.append(u) 
    if u not in p: # jak wierzchołek nie ma rodzica, to najwyraźniej s = k
        return sp
    if p[u] in Tz: # jak poprzednik wierzchołka jest w Tz to trzeba go dodać do listy sp
        sp.append(p[u])
    if p[u] != s: # jak poprzednik nie jest wierzchołkiem startowym to rekurencyjnie wywołuje się funkcje
        path(sp, p[u], s, p, Tz, price) # parametry te same, poza wierzchołkiem, podaje się jego poprzednika
    # w ten sposób rekurencyjnie tworzy się listę od docelowego wierzchołka do startowego
    return list(reversed(sp)), price # zwraca krotkę (lista, koszt)
    

def A_star(s, k, G, G_weights, G_estimation):
    Tz = [] # zbiór wierzchołków odwiedzonych
    To = [s] # zbiór wierzchołków nieodwiedzonych
    g = {}  # aktualny koszt osiagnięcia wierzchołka z wierzchołka s
    f = {} # funkcja kosztu  g + h
    p = {} # zbiór przechowujący wierzchołek -> poprzednik
    g[s] = 0 # koszt dla wierzchołka s to 0
    sp = [] # najkrótsza droga od s do k

    for u in G:   # Pętla wpisująca inf dla każdego wierzchołka w f
        f[u] = np.inf   # Rzeczywista wartość zostanie policzona później
    f[s] = 0   # element startowy znajduje się u celu, więc f = 0

    while To:   # dopóki nie sprawdzono wszystkich wierzchołków
        min = np.inf    # wyszukiwanie arg_min, w tym celu potrzeba minimalnej (na start maksymalnej) wartości
        arg_min = None   # zwracany element
        for u in To:   # wyszukiwanie arg_min wśród u w To
            if f[u] < min:  # jak f ma mniejsze to trzeba się na niego przenieść
                min = f[u]  # ustawianie min na f (u)
                arg_min = u # jest minimalny (na razie)
        if arg_min == None: # Sprawdzenie czy arg_min == None, na wszelki wypadek, powinien być niespójny
            break
        x = arg_min  # od teraz arg_min staje się x
        if x == k:  # jeśli to szukany, to kończymy działanie
            return path(sp, k, s, p, Tz, g[k])   # funkcja wyznaczająca ścieżkę na podstawie poprzedników
        To.remove(x)  # usuwanie x z To
        Tz.append(x)  # dodawanie x do Tz
        for y in G[x]:   # Dla każdego sąsiada x
            if y in Tz:  # Jak już był sprawdzany to jest pomijany
                continue
            g_star = g[x] + G_weights(x, y)  # nowa wartość kosztu
            improv = False  
            if y not in To:  # Jeśli y nie jest w głównej kolejce do zbadania
                To.append(y)   # to trzeba go tam dodać
                improv = True  # i zaznaczyć, że znaleziono lepszą ścieżkę
            elif g_star < g[y]:  # jeśli już był sprawdzany, to trzeba sprawdzić czy aktualna ścieżka 
                improv = True   # ma mniejszą wagę, jak tak, to ta jest lepsza niż poprzednia
            if improv:   # jak y nie był sprawdzany, albo znaleziono lepszą ścieżke
                p[y] = x  # dodawanie x jako poprzednika y
                g[y] = g_star  # ustawienie kosztu y jako tego wyliczonego
                f[y] = g[y] + G_estimation(y, k) # nowa wartość całościowej funkcji kosztu
    # W tym miejscu funkcja znajduje się dla niespójnego grafu
    return None
            