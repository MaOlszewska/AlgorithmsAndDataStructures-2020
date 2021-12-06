'''
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
'''

# SORTOWANIE WYRAZÓW O TEJ SAMEJ DLUGOSCI   # O(d( n + k))  k-liczba róznych cyfr , d = liczba cyfr w liczbach,
def radix(A, n, d):
    for i in range(d-1, -1, -1):
        for j in range(0, n):
            k = 0
            while k + j < n - 1:
                if A[k][i]  > A[k + 1][i]:
                    A[k], A[k + 1] = A[k + 1], A[k]
                k += 1
    return A

def repeat(S, k, n):
    tab = []
    i = 0
    for j in range(n - k + 1):
        tab.append(S[i: j + k])
        i += 1

    tab = radix(tab, len(tab), k)
    count = 1
    maxcount = 0
    i = 1
    while i <= len(tab) - 1:
        if tab[i - 1] == tab[i]:
            count += 1
            if count > maxcount:
                maxcount = count
                repeated = tab[i]
        else:
            count = 1
        i += 1
    print(maxcount, repeated)

S = 'aabbbbababababaaaabababbabababbbbababaababbbabaababaaaaabababab'
repeat(S, 6, len(S))