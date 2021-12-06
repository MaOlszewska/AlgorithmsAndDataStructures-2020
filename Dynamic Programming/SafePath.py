'''
Dana jest macierz o rozmiarze MxN, zawierająca komórki bezpieczne (o wartości 0 lub 1)
oraz niebezpieczne (-1). Należy znaleźć ścieżkę o największej liczbie "1", zaczynając
z komórki matrix[0][0]; możemy poruszać się tylko po komórkach bezpiecznych oraz
w wierszach parzystych możemy iść tylko w dół lub w prawo, natomiast w nieparzystych
- w dół lub w lewo.
'''

'''Tworzymy tablice o wymairach MxN, gdzie komórka DP[i][j] bedzie oznaczać wartość najdłuzszej ścieżki konczącej 
się w tym miejscu. Jesli wartość macierzy jest w komórce i j jest równa -1, to DP[i][j] = 0, bo nie mozemy stanąć na to pole.
Pamietamy by nie wyjść poza macierz, jeśli jeśtesmy w wierzu parzystym to bierzemy wartość z góry lub z lewej,
jeśli w nieparzystym to z prawej i z góry'''


def safe_path(M):
    n = len(M)
    DP = [[0 for _ in range(n)] for _ in range(n)]
    best_path = 0
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                if M[i][j] == -1:
                    DP[i][j] = 0
                elif i == 0 and j == 0:
                    DP[i][j] = M[i][j]
                else:
                    up = left = 0
                    if i - 1 >= 0 and j >= 0 and i - 1 < n and j < n:
                        up = DP[i - 1][j]
                    if i >= 0 and j - 1 >= 0 and i < n and j - 1 < n:
                        left = DP[i][j - 1]
                    if up > left:
                        best = up
                    else:
                        best = left
                    if best != 0:
                        DP[i][j] = best + M[i][j]
                        if DP[i][j] > best_path:
                            best_path = DP[i][j]
                    else:
                        DP[i][j] = 0
        else:
            for j in range(n):
                if M[i][j] == -1:
                    DP[i][j] = 0
                elif i == 0 and j == 0:
                    DP[i][j] = M[i][j]
                else:
                    up = right = 0
                    if i - 1 >= 0 and j >= 0 and i - 1 < n and j < n:
                        up = DP[i - 1][j]
                    if i >= 0 and j + 1 >= 0 and i < n and j + 1 < n:
                        right = DP[i][j + 1]
                    if up > right:
                        best = up
                    else:
                        best = right
                    if best != 0:
                        DP[i][j] = best + M[i][j]
                        if DP[i][j] > best_path:
                            best_path = DP[i][j]
                    else:
                        DP[i][j] = 0

    return best_path

M = [
        [1,1,1,1,1],
        [1,0,0,1,1],
        [1,1,-1,1,1],
        [-1,1,1,1,1],
        [1,1,-1,-1,1]
    ]

print(safe_path(M))

