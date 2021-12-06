'''
Proszę zaimplementować funkcję:
SumBetween(T[], od, do, n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od od do do (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).
'''


def partition(T, left, right):
    pivot = T[right]
    j = left
    for i in range(left, right + 1):
        if T[i] <= pivot:
            T[i], T[j] = T[j], T[i]
            j += 1
    return j - 1


def quick_select(T, left, right, k):
    if left == right:
        return T[left]
    mid = partition(T, left, right)
    if mid == k:
        return T[mid]
    elif k < mid:
        quick_select(T, left, mid - 1, k)
    else:
        quick_select(T, mid + 1, right, k)


def SumBetween(T, od, do, n):
    quick_select(T, 0 , n - 1, od)
    quick_select(T, od + 1, n - 1, do)
    sum = 0
    print(T)
    for i in range( od, do + 1):
        sum += T[i]
    return sum
