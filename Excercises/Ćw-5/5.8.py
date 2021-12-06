'''
Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie
'''

# DP[i][j] = koszt wejscia na pole i,j
# DP[0][j] = DP[0][j - 1] + A[0][j]
# DP[i][0] = DP[i -1][0] + A[i][0]
# Dp[0][0] = A[0][0]
# DP[i][j] = min(DP[i][j - 1], DP[i - 1][j]) + A[i][j]


def chess_board(A, n):
    DP = [[0 for _ in range(n)] for _ in range(n)]
    DP[0][0] = A[0][0]

    for i in range(1, n):
        DP[0][i] = DP[0][i - 1] + A[0][i]
        DP[i][0] = DP[i - 1][0] + A[i][0]

    for i in range(1, n):
        for j in range(1, n):
            DP[i][j] = min(DP[i][j - 1], DP[i - 1][j]) + A[i][j]
    return DP[n - 1][n - 1]
