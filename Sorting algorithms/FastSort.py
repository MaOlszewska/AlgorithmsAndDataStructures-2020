'''
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała większa od 1,
zaś x to liczby rzeczywiste  rozłożone równomiernie na przedziale [0,1]. Napisz funkcję,
która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i zwraca tablicę z wynikami eksperymentu
posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej.
'''

from math import log

def bucketSort(x, T):
    n = len(x)
    bucket = [[] for _ in range(n)]
    for j in range(len(x)):
        ind = int(n * x[j])
        bucket[ind].append(T[j])

    for i in range(n):
        bucket[i] = sorted(bucket[i])

    t = []
    for i in range(n):
        t += bucket[i]
    return t

def fast_sort(T, a):
    n = len(T)
    x = [log(T[i], a) for i in range(n)]
    T = bucketSort(x, T)
    return T


T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]

fast_sort(D1, 2)