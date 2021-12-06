'''
Dany jest zbiór przedziałów otwartych A = {(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm
(bez implementacji), który znajduje taki zbiór X, X ⊆ {1, ..., n} że (a) |X| = k (gdzie k ∈ N to
dany parametr wejściowy), (b) dla każdych i, j ∈ X, przedziały (ai, bi) oraz (aj, bj ) nie nachodzą
na siebie, oraz (c) wartość maxj∈Xbj − mini∈Xai jest minimalna. Jeśli podzbioru spełniającego
warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
'''


def kIntervals(A, k):
    A = sorted(A,key =  lambda x: x[0])
    result = [A[0]]
    count = 1
    best_result = 0
    value_min = float('inf')
    for i in range(1, len(A)):
        if count < k:
            if A[i][0] > result[count - 1][1]:
                count += 1
                result.append(A[i])
        if count == k:
            value = result[k - 1][1] - result[0][0]
            if value < value_min:
                value_min = value
                best_result = result[:]
            result.pop(0)
            count -= 1

    if best_result == 0:
        return False
    else:
        return best_result, value_min

