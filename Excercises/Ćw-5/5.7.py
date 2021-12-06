'''
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).
'''


'''
w tablicy przechowuje minimalną ilość monet dla danej kwoty (rownej indeksowi)
dla kazdego elementu szukam najmniejszego rozkladu
jezeli pierwszy nominal "miesci sie" w danej kwocie, jesli nie to następne też odpadają.
zakladam ze dla pierwszego nominalu jest najlepsza opcja
sprawdzam nominaly,dla ktorego jezeli go wezme, to łączna liczba monet bedzie najmniejsza
póki nominaly mieszcza sie w kwocie, to sprawdzam dla ktorego z nich ilosc monet bedzie najmniejsza
'''
def coin_change(coins, T):
    DP = [0 for _ in range(T)]  # ilość potrzebnych moent do wymiany kwoty i.

    for i in coins:
        DP[i] = i

    for i in range(1, T + 1):
        for j in coins:
            if i - j >= 0:
                DP[i] = min(DP[i - j] + 1, DP[i])
    return DP[T]
