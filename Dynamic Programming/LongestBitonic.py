'''
Dana jest tablica, mamy znaleźć najdłuższy podciąg (niekoniecznie spójny),
którego elementy są najpierw posortowane rosnąco, a następnie malejąco,
'''

''' Musimy mieć dwie tablice- w jedenj trzymamy najdłuższy podciag rosnący kończący się w T[i], a w drugiej
przechowujemy najdłuższy podciąg zaczynający się w T[i]. Póxnije dla każdego sprawdzamy
indeksu wartość sumy T1[i] + T2[i] - 1 i wybiermay najikszą z nich, któa jest długoscią naszego podciagu  zadania.
'''

def longest_bitonic(T):
    T1 = [1 for _ in range(len(T))]
    T2 = [1 for _ in range(len(T))]

    for i in range(2, len(T)):
        for j in range(i):
            if T[i] > T[j]:
                T1[i] = max(T1[i], T1[j] + 1)

    for i in range(len(T) - 2, -1, -1):
        for j in range( i + 1, len(T)):
            if T[i] > T[j]:
                T2[i] = max(T2[i], T2[j] + 1)
    longest = 0
    for i in range(len(T)):
        longest = max(longest, T1[i] + T2[i] - 1)
    return longest
