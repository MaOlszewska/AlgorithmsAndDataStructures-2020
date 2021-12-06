'''Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie
'''

def chessboard(T, n):
    DP = [[None for _ in range(n)] for _ in range(n)]
    DP[0][0] = T[0][0]
    for i in range(1, n):
        DP[0][i] = DP[0][i - 1] + T[0][i]
        DP[i][0] = DP[i - 1][0] + T[i][0]

    for i in range(1, n):
        for j in range(1, n):
            DP[i][j] = min(DP[i][j - 1], DP[i - 1][j]) + T[i][j]

    return DP[n - 1][n - 1]

T = [[1,2,3,4,5],
    [6,4,2,5,1],
    [4,6,8,3,1],
    [1,2,5,3,2],
    [5,4,3,6,8]]

print(chessboard(T, len(T)))