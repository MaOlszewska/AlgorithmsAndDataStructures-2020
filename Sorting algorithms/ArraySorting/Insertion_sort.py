def insert_sort(T):
    for i in range(1, len(T)):
        value = T[i]
        k = i - 1
        while k >= 0 and T[k] > value:
            T[k + 1] = T[k]
            k = k - 1
        T[k + 1] = value
    return T

