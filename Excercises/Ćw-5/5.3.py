'''
Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n^2)).
'''

'''
W tablicy przechowujemy długośc najdłuzszego podciągu utworzonego z  i liczb z A i z j liczb z B.
Jezeli liczby są równe to dokładamy do odpowidniego meijsca w tablicy wartosc z poprzendiego pola + 1, bo ciąg sie wydłuża.
Jeżeli wartosci liczb są różne to bierzemy lepszą z awartości dp[i-1][j] lub dp[i][j-1].
'''

def LCS(A, B):
    n = len(A)
    m = len(B)
    DP = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
    return DP[n][m]