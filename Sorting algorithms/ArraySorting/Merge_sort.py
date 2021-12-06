def mergeSort(T):  # sortowanie przez scalanie REKURENCYJNE  O(nlogn)
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1

    return T

def mergesort(T): #  ITERACYJNE
    l = len(T)
    for j in range(1, l):
        j *= 2
        for i in range(0, l, j):
            T1 = T[i:i + (j // 2)]
            T2 = T[i + (j // 2):j - i]
            k = m = 0
            while k < len(T1) and m < len(T2):
                if T1[k] < T2[m]:
                    m += 1
                elif T1[k] > T2[m]:
                    T1[k], T2[m] = T2[m], T1[k]
                    k += 1
            T[i:i + (j // 2)], T[i + (j // 2):j - i] = T1, T2

    return T
