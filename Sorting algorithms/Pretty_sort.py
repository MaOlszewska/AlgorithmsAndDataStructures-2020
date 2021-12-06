'''
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T) która sortuje elementy tablicy T od najładniejszych do najmniej ładnych.
'''

def counting_sort_single(T, k): # O(n + k)  Sortowanie malejące
    count = [0] * k
    newT = [0] * len(T)
    for i in range(len(T)):
        count[T[i][0]] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for i in range(len(T) - 1, -1, -1):
        count[T[i][0]] -= 1
        newT[count[T[i][0]]] = T[i]
    for i in range(len(T)):
        T[i] = newT[i]
    return T


def counting_sort_multiple(T, k): # O(n + k)   # Sortowanie rosnące
    count = [0] * k
    newT = [0] * len(T)
    for i in range(len(T)):
        count[T[i][1]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(T) - 1,-1,-1):
        newT[count[T[i][1]] -1] = T[i]
        count[T[i][1]] -= 1
    for i in range(len(T)):
        T[i] = newT[i]
    return T


def how_many_digits(number, digits):
    while number > 0:
        digit = number % 10
        digits[digit] +=1
        number = number // 10
    return digits


def pretty_sort(T):
    pretty_number = []
    for i in range(len(T)):
        digits = [0 for _ in range(10)]
        how_many_digits(T[i], digits)
        single = 0
        multiple = 0
        for j in range(10):
            if digits[j] == 1:
                single += 1
            elif digits[j] >= 1:
                multiple += 1
        pretty_number.append((single, multiple, T[i]))

    counting_sort_single(pretty_number, 10)
    counting_sort_multiple(pretty_number, 10)

    for i in range(len(T)):
        pretty_number[i] = pretty_number[i][2]
    return pretty_number


T = [114577, 1266, 455, 123, 67333, 2344 ]
print(pretty_sort(T))

