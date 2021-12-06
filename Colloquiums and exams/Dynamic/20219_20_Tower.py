'''
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie siędo pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai,bi. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.
'''

'''
dp[i][j] = najdłuzszy zakonczony na j z poprzednim i'''

def tower1(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif A[j][0] >= A[i][0] and A[j][1] <= A[i][1]:
                dp[i][j] = max(dp[x][i] for x in range(n)) + 1
    result = -1
    for i in range(n):
        Max = max(dp[i])
        result = max(result, Max)
    return result
