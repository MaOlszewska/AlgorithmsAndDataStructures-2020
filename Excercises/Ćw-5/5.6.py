'''
Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości
 (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości
'''

'''
nieskonczone, zresztą jest do niczego .
'''



def maximin(T, k):
    DP = [[0 for _ in range(k + 1)] for _ in range(len(T) + 1)]
    count = 0
    C = [0 for _ in range(len(T))]
    for i in range(1, len(T)):
        count += T[i]
        C[i] = count

    for i in range(1, len(T) + 1):
        for o in range(1, i):
            for t in range(1, k + 1):
                DP[i][t] = min(DP[i - o][t - 1], DP[0][t] - DP[0][o])
    print(DP)

A = [1, 2, 3, 2, 4, 6, 11, 1, 12, 13, 2, 3, 0]
B = [12, 0, 0, 12, 0, 0, 12, 0, 0, 12, 0, 0]
C = [100, 99, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 2

maximin(A, k)

