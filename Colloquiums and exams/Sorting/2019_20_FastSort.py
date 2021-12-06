'''
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała większa od 1 (a > 1)
zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej.
Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową
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


def fast_sort(tab, a):
    n = len(tab)
    x = [log(tab[i], a) for i in range(n)]
    tab = bucketSort(x, tab)
    return tab