def integer_knapsack(weights, profits, availability, capacity):
    # weights - wektor wag przedmiotów
    # profits - macierz zysków, gdzie profits[i][k] to zysk za (k+1)-szą sztukę i-tego przedmiotu
    # availability - wektor dostępności, czyli maksymalna liczba sztuk danego przedmiotu
    # capacity - maksymalna pojemność plecaka (ograniczenie wagowe)

    n = len(weights)  # liczba przedmiotów

    # dp[i][w] przechowuje maksymalny zysk dla przedmiotów od i do końca przy pojemności w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # decisions[i][w] przechowuje liczbę wybranych sztuk i-tego przedmiotu przy pojemności w
    decisions = [[0] * (capacity + 1) for _ in range(n)]

    # iteracja po przedmiotach od ostatniego do pierwszego
    for i in range(n - 1, -1, -1):
        # iteracja po pojemnościach od 0 do capacity
        for w in range(capacity + 1):
            max_val = dp[i + 1][w]  # zysk bez wybrania i-tego przedmiotu
            max_k = 0
            total_profit = 0

            # sprawdzenie możliwych ilości i-tego przedmiotu do wybrania
            for k in range(1, availability[i] + 1):
                total_weight = k * weights[i]
                if total_weight <= w:
                    total_profit += profits[i][k - 1]  # suma zysków z k sztuk
                    val = total_profit + dp[i + 1][w - total_weight]  # całkowity zysk po 
                    # dodaniu pozostałych przedmiotów
                    if val > max_val:
                        max_val = val
                        max_k = k
                else:
                    break  # dalsze zwiększanie k przekracza pojemność

            dp[i][w] = max_val  # zapis maksymalnego zysku
            decisions[i][w] = max_k  # zapis optymalnej liczby sztuk i-tego przedmiotu

    strategy = [0] * n
    remaining_capacity = capacity

    # odtworzenie strategii na podstawie macierzy decyzji
    for i in range(n):
        k = decisions[i][remaining_capacity]
        strategy[i] = k
        remaining_capacity -= k * weights[i]

    max_profit = dp[0][capacity]  # maksymalny zysk dla pełnej pojemności i wszystkich przedmiotów
    return dp, decisions, max_profit, strategy