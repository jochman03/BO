def johnson_2(tasks): # Algorytm Johnsona dla dwóch maszyn
    # tasks - lista krotek: (index, czas maszyny 1, czas maszyny 2)
    n = len(tasks) # liczba zadań
    start = 0 # indeks pierwszego zadania
    end = n - 1 # indeks ostatniego zadania
    order = [None] * n # lista do przechowywania kolejności zadań
    details = tasks[:] # tymczasowa lista zadań
    
    while details: # dopóki lista details nie jest pusta
        min_detail = min(details, key=lambda x: min(x[1], x[2])) # wyszukiwanie zadania z najmniejszym czasem
        i, t1, t2 = min_detail # rozpakowanie krotki

        if t1 <= t2: #  jeśli czas znajduje się w pierwszym rzędzie 
            order[start] = i # to ląduje na początku sortowanej listy
            start += 1  # inkrementacja indeksu początku
        else: # jeśłi jest w drugim rzędzie
            order[end] = i  # to ląduje na końcu
            end -= 1 # dekrementacja indeksu końca

        details.remove(min_detail) # usuwanie zadania z tymczasowej listy

    return order # zwracanie kolejności (bez czasów)

def cds_algorithm(times): # algorytm CDS
    # times - macierz n x m - zadania x maszyny
    n = len(times)    # ilość zadań
    m = len(times[0]) # ilość maszyn
    best_order = None # tymczasowa zmienna do przechowywania najlepszej kolejności
    best_times = None # zmienna przechowująca najlepszą macierz czasów

    best_makespan = float('inf') # najlepszy minimalny czas realizacji
    for r in range(1, m): # dla r w zakresie 1, m-1
        times_2d = [] # tymczasowa lista przekazywana do algorytmu johnsona
        for i in range(n): # dla każdego zadania
            time_a = sum(times[i][:r]) # czas maszyny 1
            time_b = sum(times[i][-r:])  # czas maszyny 2
            times_2d.append((i, time_a, time_b)) # uzupełnianie tymczasowej listy
        
        order = johnson_2(times_2d) #  tworzenie pomocniczego zadania dla 2 maszyn

        # wyznaczanie czasu realizacji
        end_times = [[0]*m for _ in range(n)] # pomocnicza macierz

        for i, task in enumerate(order):#
            for j in range(m):          # iteracja po elementach macierzy
                if i == 0 and j == 0: # pierwszy element
                    end_times[i][j] = times[task][j] # czas realizacji to jego czas
                elif i == 0: # element w pierwszym rzędzie, czas realizacji to czas elemenu z
                    end_times[i][j] = end_times[i][j-1] + times[task][j] #  poprzedniej kolumny i poprzedniego
                    #wiersza oraz jego czas realizacji
                elif j == 0: # element w pierwszej kolumnie, jego wartość to czas elementu w
                    # poprzednim wierszu i jego czas realizacji
                    end_times[i][j] = end_times[i-1][j] + times[task][j]
                else: # pozostałe elementy, wyznaczana jest maksymalna wartość z elementu po 
                    # prawej w macierzy i powyżej, do tego dodaje się czas realizcji
                    end_times[i][j] = max(end_times[i-1][j], end_times[i][j-1]) + times[task][j] 

        # całkowity czas realizacji jako kryterium sortowania
        current_makespan = end_times[-1][-1] # ostatni element to całkowity czas
        if current_makespan < best_makespan: # jak jest mniejszy to zastępuje najlepszy
            best_makespan = current_makespan
            best_order = order
            best_times = end_times

    return best_order, best_makespan, best_times