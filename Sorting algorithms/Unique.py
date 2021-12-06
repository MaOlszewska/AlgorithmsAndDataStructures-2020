'''
Proszę zaimplementować funkcję:  count(arr);
Funkcja ta przyjmuje na wejściu posortowaną tablicę n liczb całkowitych, w której mogą pojawiać się duplikaty.
Funkcja powinna zliczać ilość wystąpień różnych wartości bezwzględnych elementów występujących w tej tablicy.
'''

def count(T):
    left = 0
    right = len(T) - 1
    count = len(T)
    while left <= right:  # kiedy obok siebie są takie same liczby
        while left != right and T[left] == T[left + 1]:
            left += 1
            count -= 1
        while left != right and T[right] ==T[right - 1]:
            right -= 1
            count -= 1

        if left == right:
            break

        suma = T[left] + T[right]
        if suma == 0:
            count -= 1
            left += 1
            right -= 1
        elif suma < 0:
            left += 1
        else:
            right -= 1
    return count

