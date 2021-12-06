'''
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest
sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową
'''

def sum(T):
    sorted(T)
    for number in T:
        i = 0
        j = len(T) - 1
        while i != j:
            if T[i] + T[j] == number:
                break
            elif T[i] + T[j] < number:
                i += 1
            else:
                j -= 1
        if i == j:
            return False
    return True

