'''Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
ze zbioru 0, . . . , n2 − 1.
'''

def countSort(T, n, exp):
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[i] = 0

    for i in range(n):
        C[(T[i] // exp) % n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[(T[i] // exp) % n] - 1] = T[i]
        C[(T[i] // exp) % n] -= 1

    for i in range(n):
        T[i] = B[i]


def sort(T):
    countSort(T, len(T), 1)
    countSort(T, len(T), len(T))