'''
(problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący wartość
optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym.
Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów.
'''


def knapsack(W, P, MaxW):
    n = len(W)
    sum_ = sum(P)
    w = sum(W)
    DP = [[0] + [w + 1] * sum_ for _ in range(n)]
    DP[0][P[0]] = W[0]
    for i in range(1, n):
        for p in range(sum_ + 1):
            if p < P[i]:
                DP[i][p] = DP[i - 1][p]
            else:
                DP[i][p] = min(DP[i - 1][p], DP[i - 1][p - P[i]] + W[i])
    for p in range(sum_, -1, -1):
        if DP[n - 1][p] != w + 1 and DP[n - 1][p] <= MaxW:
            return p, DP
    return None, None


def getsolution(DP, W, P, i, p):
    if p == 0:
        return []
    if i == 0:
        return [0]
    if DP[i - 1][p] == DP[i][p]:
        return getsolution(DP, W, P, i - 1, p)
    return getsolution(DP, W, P, i - 1, p - P[i]) + [i]