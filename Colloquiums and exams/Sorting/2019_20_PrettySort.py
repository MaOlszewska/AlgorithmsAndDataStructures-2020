'''
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''

def counting_sort_single(T, k): # O(n + k)  Sortowanie malejące
    count = [0] * k
    newT = [0] * len(T)
    for i in range(len(T)):
        count[T[i][1]] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for i in range(len(T) - 1, -1, -1):
        count[T[i][1]] -= 1
        newT[count[T[i][1]]] = T[i]
    for i in range(len(T)):
        T[i] = newT[i]
    return T


def counting_sort_multiple(T, k): # O(n + k)   # Sortowanie rosnące
    count = [0] * k
    newT = [0] * len(T)
    for i in range(len(T)):
        count[T[i][2]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(T) - 1,-1,-1):
        newT[count[T[i][2]] -1] = T[i]
        count[T[i][2]] -= 1
    for i in range(len(T)):
        T[i] = newT[i]


def numbers(number):
    T = [0 for _ in range(10)]
    while number > 0:
        T[number % 10] += 1
        number //= 10
    return T

def counter(A):  # (liczba, ilość jednokrotnych, ilośc wielokrotnych)
    for i in range(len(A)):
        T = numbers(A[i])
        jedno = 0
        wielo = 0
        for j in range(10):
            if T[j] == 1:
                jedno += 1
            elif T[j] > 1:
                wielo += 1
        A[i] = (A[i], jedno, wielo)
    return A

def pretty_sort(A):
    A = counter(A)
    counting_sort_single(A, 10)
    counting_sort_multiple(A, 10)
    for i in range(len(A)):
        A[i] = A[i][0]
    return A
A = [114577, 1266, 455, 123, 67333, 2344]
print(pretty_sort(A))