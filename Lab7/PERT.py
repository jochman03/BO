class Task: # Klasa reprezentująca czynność
    def __init__(self, id, start, end, t_c, t_m, t_p):  # id, zdarzenie początkowe, zdarzenie końcowe
        # czas optymistyczny, prawdopodobny, pesymistyczny
        self.id = id # identyfikator zadania
        self.start = start # zdarzenie początkowe
        self.end = end # zdarzenie końcowe
        self.t_c = t_c # czas optymistyczny
        self.t_m = t_m # czas prawdopodobny
        self.t_p = t_p # czas pesymistyczny
        self.t_0 = (t_c + 4*t_m + t_p) / 6 # czas oczekiwany
        self.L = 0 # rezerwa czasowa
        self.sigma_2 = 0 # wariancja


class Event: # Klasa reprezentująca zdarzenie
    def __init__(self, id): # id zdarzenia
        self.id = id # identyfikator zdarzenia
        self.early_time = 0 # czas najwcześniejszy
        self.late_time = float('inf') # czas najpóźniejszy
        self.incoming = [] # lista zadań przychodzących
        self.outgoing = [] # lista zadań wychodzących


def PERT(events, tasks): # Funkcja PERT
    # przypisanie zadań do zdarzeń
    for task in tasks: # Iteracja po zadaniach
        events[task.start].outgoing.append(task) # dodanie zadania do zdarzenia początkowego
        events[task.end].incoming.append(task) # dodanie zadania do zdarzenia końcowego

    # wyznaczenie porządku topologicznego zdarzeń
    sorted_events = [] # lista posortowanych zdarzeń
    visited = set() # zbiór odwiedzonych zdarzeń

    def visit(event): # Funkcja rekurencyjna do odwiedzania zdarzeń
        if event.id in visited: # jeśli zdarzenie zostało odwiedzone, to zwróć
            return 
        visited.add(event.id) # dodaj zdarzenie do zbioru odwiedzonych
        for task in event.incoming: # iteracja po zadaniach przychodzących
            visit(events[task.start]) # odwiedź zdarzenie początkowe
        sorted_events.append(event) # dodaj zdarzenie do listy posortowanych zdarzeń

    for event in events.values(): # iteracja po zdarzeniach
        visit(event) # odwiedź zdarzenie

    # wyznaczenie czasu najwcześniejszego dla zdarzeń
    for event in sorted_events: # iteracja po posortowanych zdarzeniach
        for task in event.incoming: # iteracja po zadaniach przychodzących
            task_end_time = events[task.start].early_time + task.t_0 # czas zakończenia zadania
            event.early_time = max(event.early_time, task_end_time)  # aktualizacja czasu najwcześniejszego

    # wyznaczenie czasu najpóźniejszego dla zdarzeń
    project_duration = max(e.early_time for e in events.values()) # czas trwania projektu
    for event in events.values(): # iteracja po zdarzeniach
        if not event.outgoing: # jeśli zdarzenie nie ma zadań wychodzących
            event.late_time = project_duration # ustawienie czasu najpóźniejszego na czas trwania projektu
 
    for event in reversed(sorted_events): # iteracja po posortowanych zdarzeniach w odwrotnej kolejności
        for task in event.outgoing: # iteracja po zadaniach wychodzących
            start_event = events[task.end] # zdarzenie początkowe
            task_start_latest = start_event.late_time - task.t_0 # czas najpóźniejszy rozpoczęcia zadania
            event.late_time = min(event.late_time, task_start_latest) # aktualizacja czasu najpóźniejszego

    # wyznaczenie ścieżki krytycznej i wariancji
    critical_path = [] # lista krytycznych czynności
    critical_nodes = [] # lista krytycznych zdarzeń
    total_variance = 0
    for task in tasks: # iteracja po zadaniach
        early_start = events[task.start].early_time # czas najwcześniejszy rozpoczęcia zadania
        late_start = events[task.end].late_time - task.t_0 # czas najpóźniejszy rozpoczęcia zadania
        task.L = late_start - early_start # rezerwa czasowa zadania
        task.sigma_2 = ((task.t_p - task.t_c) / 6) ** 2 # wyznaczenie wariancji zadania
        if task.L == 0: # jeśli rezerwa czasowa jest równa 0
            critical_path.append(task.id) # dodaj zadanie do ścieżki krytycznej
            total_variance += task.sigma_2
            if task.start not in critical_nodes:
                critical_nodes.append(task.start)
            if task.end not in critical_nodes:
                critical_nodes.append(task.end)

    return critical_path, critical_nodes, project_duration, total_variance 
# zwrócenie ścieżki krytycznej, czasu trwania projektu i wariancji całkowitej
