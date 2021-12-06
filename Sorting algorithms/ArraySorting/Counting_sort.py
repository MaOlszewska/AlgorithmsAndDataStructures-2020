def Counting(T, k): # O(n + k)
    C = [0] * k
    B = [0] * len(T)
    for i in range(len(T)):
        C[T[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(T) - 1, -1, -1):
        C[T[i]] -= 1
        B[C[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = B[i]
    return T
