'''
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
'''


'''
Algorytm Dynamiczny gdzie:
DP[i] = Maksymalna wartość przedmitów do i
DP[0] = A[0]
DP[1] = max(A[0],A[1])
DP[i] = max(DP[i - 1], DP[ i - 2] + A[i])
'''


def goodThief(A):
    n = len(A)
    DP = [0  for _ in range(n)]
    DP[0] = A[0]
    DP[1] = max(A[1], A[0])

    for i in range(2, n):
        DP[i] = max(DP[i - 1], DP[i - 2] + A[i])

    value = DP[n - 1]
    result = []
    for i in range(n - 1, 0, -1):
        if DP[i] == value:
            if DP[i] == DP[i - 1]:
                result.append(i - 1)
                value -= A[i - 1]
            else:
                result.append(i)
                value -= A[i]
    return result, DP[n - 1]

A = [8,4,3,5,6,7,2,3,15,10]
print(goodThief(A))