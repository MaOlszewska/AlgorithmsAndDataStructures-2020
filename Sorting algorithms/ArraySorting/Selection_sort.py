def selection_sort(T):
    l = len(T)
    for i in range(l):
        min = i
        for k in range(i + 1, l):
            if T[k] < T[min]:
                min = k
            T[i], T[min] = T[min], T[i]
    return T

