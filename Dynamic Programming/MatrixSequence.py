'''
Dana jest macierz o rozmiarze NxN. Każda z komórek ma różne wartości - od 1 do N.
Chcemy znaleźć najdłuższą sekwencję składającą się z sąsiadujących komórek, taką, że
wartość każdej kolejnej sąsiedniej komórki jest o 1 większa od poprzedniej.
'''

'''DP[i][j] - najdłuzsza sekwencja dla komórki[i][j]'''

def longest_matrix_sequence(M):
    n = len(M)
    DP = [[1 for _ in range(n)] for _ in range(n)]
    def longest(M, i, j, DP):
        if not (i >= 0 and i < n and j >= 0 and j < n):
            return  0
        elif DP[i][j] == 1:
            if i - 1 >= 0 and M[i - 1][j] == M[i][j] + 1:      # góra
                DP[i][j] = 1 + longest(M, i - 1, j, DP)
            if i + 1 < len(M) and M[i + 1][j] == M[i][j] + 1:  # Dół
                DP[i][j] = 1 + longest(M, i + 1, j, DP)
            if j + 1 < len(M) and M[i][j + 1] == M[i][j] + 1:  # prawa
                DP[i][j] = 1 + longest(M, i, j + 1, DP)
            if j - 1 >= 0 and M[i][j - 1] == M[i][j] + 1:      # lewa
                DP[i][j] = 1 + longest(M, i, j - 1, DP)
        return DP[i][j]

    longest_path = 0
    for i in range(n):
        for j in range(n):
            curr = longest(M, i, j, DP)
            if curr > longest_path:
                longest_path = curr
    return longest_path

