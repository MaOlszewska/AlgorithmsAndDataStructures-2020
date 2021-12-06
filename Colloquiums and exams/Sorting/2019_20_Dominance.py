'''
Mówimy, że punkt (x, y) słabo dominuje punkt (x′, y′) jeśli x ≤ x′oraz y ≤ y′
(w szczególności
każdy punkt słabo dominuje samego siebie). Dana jest tablica P zawierająca n punktów. Proszę
zaimplementować funkcję dominance(P), która zwraca tablicę S taką, że:
1. elementami S są indeksy punktów z P,
2. dla każdego punktu z P, S zawiera indeks punktu, który go słabo dominuje,
3. S zawiera minimalną liczbę elementów.
'''


def isNotDominated(P, i, x,y):
    n = len(P)
    for j in range(i + 1, n):
        if P[j][0] <= x and P[j][1] <= y:
            return False
    return True


def dominance(P):
    n = len(P)
    for i in range(n):
        P[i] = ((P[i][0], P[i][1], i))

    P = sorted(P, reverse=True)
    result = []

    for i in range(n):
        if isNotDominated(P, i, P[i][0],P[i][1]):
            result.append(P[i][2])
    return result




P = [ (2,2), (1,1), (2.5,0.5), (3,2), (0.5,3) ]
print(dominance(P))