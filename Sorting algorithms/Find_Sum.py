'''  Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program, który stwierdza czy istnieją
indeksy i oraz j takie, że A[i] + A[j] = x.
'''


def find_sum(A, x):
    l = 0
    r = len(A) - 1
    while True :
        if l >= r:
            return False
        if A[l] + A[r] == x:
            return True
        if A[l] + A[r] < x:
            l += 1
        else:
            r -= 1
