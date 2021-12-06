'''
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
'''

def radix(A, n, d):
    for i in range(d-1, -1, -1):
        for j in range(0, n):
            k = 0
            while k + j < n - 1:
                if A[k][i] > A[k + 1][i]:
                    A[k], A[k + 1] = A[k + 1], A[k]
                k += 1
    return A


def String_Sort(String, n, k):
    T = []
    count = 0
    for i in range(n - k + 1):
        T.append(String[count: i + k])
        count += 1

    T = radix(T, count, k)
    count, maxcount = 1, 0
    i = 1
    string = None
    while i <= len(T) - 1:
        if T[i] == T[i - 1]:
            count += 1
            if count >= maxcount:
                maxcount = count
                string = T[i]
        else:
            count = 1
        i += 1
    return string, maxcount

