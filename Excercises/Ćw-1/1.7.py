'''
Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x
'''

def search_sum(A, x):
    i = 0
    j = len(A) - 1
    while i != j:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] > x:
            j -= 1
        else:
            i += 1
    return False

