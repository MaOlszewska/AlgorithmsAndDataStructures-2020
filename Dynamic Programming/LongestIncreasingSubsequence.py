def LIS(T):
    DP = [1 for _ in range(len(T))]
    Parent = [-1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if T[j] < T[i] and DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1
                Parent[i] = j
    return (max(DP), DP, Parent)

def PrintSOlution(T, Parent, i):
    if Parent[i] != -1:
        PrintSOlution(T, Parent, Parent[i])
    print(T[i])

# W nlogn

def bin_search(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def Lis(A):
    n = len(A)
    if n == 0: return False
    if n == 1: return A[0]

    B = [0] * (n + 1)
    B[0] = A[0]
    lis_len = 1

    for i in range(1, n):
        if A[i] < B[0]:
            B[0] = A[i]
        elif A[i] > B[lis_len - 1]:
            B[lis_len] = A[i]
            lis_len += 1
        else:
            index = bin_search(B, -1, lis_len - 1, A[i])
            B[index] = A[i]
    return lis_len
