def bucketSort(T):   # DLA LICZB OD 0 do 1   O(n)
    bucket = []
    n = len(T)
    section = 1 / n

    for i in range(n):
        bucket.append([])

    for j in T:
        ind = int(j / section)
        bucket[ind].append(j)

    for i in range(n):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            T[k] = bucket[i][j]
            k += 1
    return T
