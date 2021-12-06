'''Mając tablice z liczbami dodatnimi sprawdzić zcy można ją podzielić na dwa podzbiory o równej sumie'''

'''Jesli suma wszytskich elementów jest nieprzysta to znaczy ze nie da sie podzielić zbioru na dwa.
jesli jest parzysta trzeba sprawdzić czy istniją takie dwa podzbiory.
Dp[i][j]- podzbiór z sumą j można znaleźć do pierwszych i elemetnów.
'''


def subsetSum(T):
    n = len(T)
    suma = sum(T)
    if suma % 2 != 0:
        return False
    suma = suma // 2

    DP = [[False for _ in range(suma + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        DP[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, suma + 1):
            if T[i - 1] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = DP[i - 1][j] or DP[i - 1][j - T[i - 1]]
    return DP[n][suma]