'''Proszę napisać funkcję znajdującą minimum i maksimum w tablicy o długości n, wykonując a 1.5n porównań.'''

def MinMax(T):
    min = max = T[0]

    for i in range(0, len(T), 2):
        if T[i] < T[i + 1]:
            T[i], T[i + 1] = T[i + 1], T[i]
        if T[i] > max:
            max = T[i]
        elif T[i + 1] < min:
            min = T[i + 1]
    return min, max
