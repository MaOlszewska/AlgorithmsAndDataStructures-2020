'''
Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
że x < z < y (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
których A[i + 1] − A[i] jest największe)
'''


def maxpair(T):
    n = len(T)
    Max = T[0]
    Min = T[0]
    for i in range(n):
        Max = max(Max, T[i])
        Min = min(Min, T[i])

    T1 = [[] for _ in range(n)]
    x = (Max + Min) / n

    for i in range(n):
        buckets = int((T[i] - Min) / x)
        T1[buckets].append(T[i])
    result = 0
    prevMax = max(T1[0])

    for i in range(1, n):
        if len(T1[i]) != 0:
            currMin = min(T1[i])
            result = max(result, currMin - prevMax)
            prevMax = max(T1[i])

    return result

