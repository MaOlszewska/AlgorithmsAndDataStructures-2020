'''
Dana jest macierz binarna o rozmiarze MxN. Mamy znaleźć największą kwadratową pod-macierz
składającą się wyłącznie z "1".
'''

'''
DP[i][j] - rozmiar najwiekszej podmacierzy konczące się w M[i][j], jest o jeden wiekszy niz minimum z 
podmacierzy konczących sie w M[i-1][j], M[i][j-1], M[i-1][j-1].
'''


def submatrix(M):
    n = len(M)
    DP = [[0 for _ in range(n)] for _ in range(n)]

    largest = 0
    for i in range(n):
        if M[0][i] == 1:
            DP[0][i] = 1
        if M[i][0] == 1:
            DP[i][0] = 1

    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                DP[i][j] = 0
            else:
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1
                if DP[i][j] > largest:
                    largest = DP[i][j]

    return largest
