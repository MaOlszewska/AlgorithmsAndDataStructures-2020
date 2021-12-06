'''
Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie
 jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów
A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j − i jest minimalna (innymi słowy,
szukamy najkrótszego przedziału z wszystkimi kolorami)
'''


'''
Tworzymy tablice w której bedizmey zapisywac ile aktalnie w przedziele mamy danego koloru(Tablica długości k + 1).
tworzymy licznik którym bedziemy liczyć ile mamy róznych kolorów w przedziale.
Jesli licznik jest mniejszy od liczby wsyztskich kolorów to poszerzamy nasz przedział na prawo, dodajemy do tablicy z kolorami ile mamy 
aktualnie ilosci jednego koloru, jesli licznik zrówna się z liczbą k to przesuwamy znowu indeks lewy i  sprawdzmy ile
możemy skrócić asz przedział, żeby dalej się w  nim znajwdowały wszystkie kolory.
'''
def shortest_interval(A, n, k):
    count_colors = [0 for _ in range(k + 1)]
    colors = 0
    i, j = 0,  -1
    min_j = min_i = -1
    shortest = n
    while True:
        if colors < k:
            if j == n - 1:
                break
            j += 1
            if count_colors[A[j]] == 0:
                colors += 1
            count_colors[A[j]] += 1
        if colors == k:
            if j - i < shortest:
                min_i = i
                min_j = j
                shortest = j - i
            count_colors[A[i]] -= 1
            if count_colors[A[i]] == 0:
                colors -= 1
            i += 1
    return min_i, min_j

T = [1,2,3,1,2,4,3,2,5,3,3,1]
print(shortest_interval(T, len(T), 5))