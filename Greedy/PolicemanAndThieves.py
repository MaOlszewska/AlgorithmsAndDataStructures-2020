'''
Mamy tablice o rozmiarze n, kazdy elemnt tablicy zawiera policjanta albo złodzija, każdy policjant
może złapać tylko jednego złodzieja, nie może go złapać jeśli jest w odległości większej niż K jednostek.
Należy znaleźć maksyamlną liczbe złodzieji, których moża złapać
'''

'''szukamy najmniejszego indeksu policajnta i złodzieja, jesli odległosc miedzy indeksem złodzieja i polisjanta
mniejsza albo róna k to złapano złodzieja i może przesunać indeksy.'''
def policeThief(t, k):
    P = []
    T = []
    result = 0
    for i in range(len(t)):
        if t[i] == 'P':
            P.append(i)
        else:
            T.append(i)
    l = r = 0
    while l < len(T) and r < len(P):
        if abs(T[l] - P[r]) <= k:
            result += 1
            l += 1
            r += 1
        elif T[l] < P[r]:
            l += 1
        else:
            r += 1
    return result

t = ['P', 'T', 'P', 'T', 'T', 'P']
