'''
Dana jest tablica n liczb A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać
podciąg liczb z A, które sumują się do zadanej wartości T.
'''

# f(i, s) - czy z liczb a[1] od zera do a[i] da sie otrzymac sume s
# f(n, T)

# f(i, s) = f(i - 1, s) lub f(i-1, s-a[i]) pod warunkiem, ze s - a[i] > 0
# f(0, 0) - prawda
# f(0, s) - falsz dla s > 0

def subsetsum(T, target):
    n = len(T)
    DP = [[0 for _ in range(n + 1)] for _ in range(target + 1)]
    for i in range(target + 1):
        DP[i][0] = 0
    for i in range(n + 1):
        DP[0][i] = 1
    for sum in range(1, target + 1):
        for lenght in range(1, n + 1):
            if T[lenght - 1] > sum:
                DP[sum][lenght] = DP[sum][lenght - 1]
            else:
                DP[sum][lenght] = (DP[sum][lenght - 1] or DP[sum - T[lenght - 1]][lenght - 1])
    if DP[target][n] == 1:
        return True
    return False
