''' Mając liczbę naturalną n oblicz ile minimalnie kwadratów sumuje się do tej liczby'''

''' DP[i]- minimalna liczba kwadratów sumujacych się do liczby i'''

def min_square(n):
    DP = [0 for _ in range(n + 1)]

    for i in range(n + 1):
        DP[i] = i # 1^2 * i
        j = 1
        while j * j <= i:
            DP[i] = min(DP[i], 1 + DP[i - j*j])
            j += 1
    return DP[n]
