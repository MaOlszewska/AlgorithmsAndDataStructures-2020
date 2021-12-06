'''
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy
jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
'''

def check(T, i, j, idx):
    while True:
        if i == idx:
            i += 1
        if j == idx:
            j -= 1

        if T[i] + T[j] == T[idx]:
            return True
        elif T[i] + T[j] < T[idx]:
            i += 1
        elif i == j:
            return False
        else:
            j -= 1

def sumoftwo(T):
    T = sorted(T)
    for i in range(len(T)):
        if not check(T, i, 0, len(T) - 1):
            return False
    return True

