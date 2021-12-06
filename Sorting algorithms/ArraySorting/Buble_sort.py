def bubble_sort(T):
    for i in range(len(T) - 1):
        for j in range(len(T) - 1 - i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T
