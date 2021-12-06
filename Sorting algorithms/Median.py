'''wyszukiwanie itego co do wielkosci elemntu '''

def median(T, i):
    lists = [T[j:j + 5] for j in range(0, len(T), 5)]
    medians = [sorted(j)[len(j) // 2] for j in lists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median(medians, len(medians) // 2)

    lower = []
    greater = []
    for i in T:
        if i >= pivot:
            greater.append(i)
        else:
            lower.append(i)

    idx_pivot = len(lower)
    if i < idx_pivot:
        return median(lower, i)
    elif i > idx_pivot:
        return median(greater, i - idx_pivot - 1)
    return pivot

