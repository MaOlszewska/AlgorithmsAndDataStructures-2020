'''
Dany jest zbiór punktów X = {x1, . . . , xn} na
prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
'''

'''
Należy posortować punkty rosnąco. Poźniej utorzyc pierwszy przedział [X[0], X[0] + 1], pożniej bierzemy kolejne
liczby z posortowanej tablicy i sprawdzamy czy one mieszczą się w naszym aktualnym przedziale. Jeśli się mieszczą 
to sprawdzam kolejne, jesli nie, to tworzę nowy aktulany przedział i zwiększam licznik przedziałów.
'''

def interval(X):
    intervals = 0
    current = []
    X = sorted(X)

    for i in X:
        if len(current) == 0:
            current = [i, i + 1]
        elif i > current[1]:
            intervals += 1
            current = [i, i + 1]
    intervals += 1

    return intervals

X = [ 1.4, 0.3, 3,3.4, 5, 2.8, 3.9]
print(interval(X))