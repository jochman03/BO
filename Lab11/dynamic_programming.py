import sys

def optimal_production_plan(q, g, h, Ymin, Ymax, y0, y_end):
    # q     - lista zapotrzebowania na produkt w kolejnych miesiącach
    # g     - lista kosztów produkcji dla każdej wielkości produkcji
    # h     - lista kosztów magazynowania dla każdego stanu magazynu
    # Ymin  - minimalny dopuszczalny stan magazynu
    # Ymax  - maksymalny dopuszczalny stan magazynu
    # y0    - stan magazynu na początku planu (przed pierwszym miesiącem)
    # y_end - wymagany stan magazynu po ostatnim miesiącu

    n = len(q)  # liczba miesięcy w planie

    # dp[i] to słownik: klucz = stan magazynu po i-tym miesiącu,
    # wartość = minimalny koszt dojścia do tego stanu
    dp = [dict() for _ in range(n + 1)]

    # decisions[i] to słownik decyzji dla miesiąca i:
    # klucz = stan magazynu po i-tym miesiącu,
    # wartość = (stan magazynu przed miesiącem, wielkość produkcji)
    decisions = [dict() for _ in range(n)]

    # koszt na początku dla stanu magazynu y0
    dp[0][y0] = 0

    # przejście przez kolejne miesiące
    for i in range(n):
        # iteracja po możliwych stanach magazynu przed miesiącem i
        for y_prev in dp[i]:
            # sprawdzenie wszystkich dopuszczalnych wielkości produkcji
            for x in range(0, Ymax + 1):
                # obliczenie stanu magazynu po produkcji i zużyciu zapotrzebowania
                y_next = y_prev + x - q[i]

                # uwzględnienie tylko stanów magazynu mieszczących się w dopuszczalnym zakresie
                if Ymin <= y_next <= Ymax:
                    # obliczenie kosztu produkcji i magazynowania
                    cost = g[x] + h[y_next]

                    # obliczenie całkowitego kosztu dojścia do nowego stanu
                    total_cost = dp[i][y_prev] + cost

                    # aktualizacja minimalnego kosztu i decyzji, jeśli znaleziono lepsze rozwiązanie
                    if y_next not in dp[i + 1] or total_cost < dp[i + 1][y_next]:
                        dp[i + 1][y_next] = total_cost
                        decisions[i][y_next] = (y_prev, x)

    # sprawdzenie, czy możliwe jest osiągnięcie wymaganego stanu końcowego magazynu
    if y_end not in dp[n]:
        raise ValueError("Nie można osiągnąć końcowego stanu magazynu.")

    # odtworzenie optymalnej strategii produkcji od końca
    strategy = [0] * n
    y = y_end
    for i in range(n - 1, -1, -1):
        y_prev, x = decisions[i][y]
        strategy[i] = x
        y = y_prev

    min_cost = dp[n][y_end]

    # dp       - tablica słowników z minimalnymi kosztami dojścia do danego stanu w każdym miesiącu
    # decisions- tablica słowników z decyzjami produkcyjnymi prowadzącymi do danego stanu
    # min_cost - minimalny całkowity koszt realizacji planu produkcji i magazynowania
    # strategy - lista optymalnych wielkości produkcji dla kolejnych miesięcy
    return dp, decisions, min_cost, strategy