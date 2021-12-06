'''
Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie
jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
szukamy najkrótszego przedziału z wszystkimi kolorami).
'''

def Colors( T ,n, k):
    colors = 0
    B = [0 for _ in range(k)]
    i = 0
    j = -1
    min_i = min_j = -1
    shortest = n
    while True:
        if colors < k:
            if j == n - 1:
                break
            j += 1
            if B[T[j]] == 0:
                colors += 1
            B[T[j]] += 1
        if colors == k:
            if j - i < shortest:
                min_i, min_j = i, j
                shortest = j - i
            B[T[i]] -= 1
            if B[T[i]] == 0:
                colors -= 1
            i += 1
    return (min_i, min_j)
