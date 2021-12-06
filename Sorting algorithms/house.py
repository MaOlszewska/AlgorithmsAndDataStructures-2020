'''
Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi,
w którym z nich należy wybudować dom, tak aby suma euklidesowych odległości od tego punktu
do wszystkich pozostałych była minimalna. Należy zwrócić również tę sumę.
Algorytm powinien być jak najszybszy.
'''

def distance(T):
    T = sorted(T)
    prev = 0
    next = sum(T) - T[0]

    minsum = next - T[0] * (len(T) - 1)
    idx = 0
    for i in range(1, len(T)):
        prev += T[i - 1]
        next -= T[i]
        if minsum > T[i] * i - prev - T[i] * (len(T) - 1 - i) + next:
            minsum = T[i] * i - prev - T[i] * (len(T) - 1 - i) + next
            idx = i

    return idx, minsum

