'''
Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.
'''

def MinMax(T):
    count = 0
    mini = maxi = T[0]
    for i in range(0, len(T), 2):
        print(i)
        count += 1
        if i + 1 == len(T):
            break
        if T[i] < T[i + 1]:
            T[i], T[i + 1] = T[i + 1], T[i]
        count += 1
        if T[i] > maxi:
            maxi = T[i]
        count += 1
        if T[i + 1] < mini:
            mini = T[i + 1]
    return maxi, mini, count
