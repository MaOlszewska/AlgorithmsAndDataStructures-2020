'''Mając tablice liczb całkowitch, należy znaleźć maksymalną sumę podciągu, w którym podcią nie zawiera
sąsiednich elementów
'''

'''DP[i] przechowuje wartości maksymalne osiagniete do indeksu i'''

def max_sum(T):
    n = len(T)
    if n == 1:
        return T[0]
    DP = [None for _ in range(n)]
    DP[0] = T[0]
    DP[1] = max(T[0], T[1])

    for i in range(2, n):
        DP[i] = max(DP[i -1], DP[i - 2] + T[i])
        DP[i] = max(DP[i], T[i])
    return DP[n - 1]