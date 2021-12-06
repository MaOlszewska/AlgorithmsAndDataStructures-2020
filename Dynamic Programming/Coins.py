'''
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)
'''


def coins(T, n):
    DP = [float('inf') for _ in range(T + 1)]
    DP[0] = 0
    for i in n:
        DP[i] = 1
    for i in range(1, T + 1):
            for j in n:
                if i - j >= 0:
                    DP[i] = min(DP[i], DP[i - j] + 1)
    return DP[T]

T = 15
n = [1,5,8]
