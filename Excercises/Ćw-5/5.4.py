'''
Proszę rozwiązać dwa następujące zadania:
1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
najdłuższego rosnącego podciągu?
2. Na wykładzie podaliśmy algorytm działający w czasie O(n^2).
Proszę podać algorytm o złożoności O(nlog n).
'''

# 1
def PrintSOlution(T, Parent, i):
    if Parent[i] != -1:
        PrintSOlution(T, Parent, Parent[i])
    print(T[i])

def LIS(T):
    DP = [1 for _ in range(len(T))]
    Parent = [-1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if T[j] < T[i] and DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1
                Parent[i] = j
    return (max(DP), DP, Parent)

# 2

