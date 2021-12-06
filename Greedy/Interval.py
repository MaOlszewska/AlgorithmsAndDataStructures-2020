'''
Dany jest zbiór punktów X = {x1, . . . , xn} na
prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
'''

def interval(X):
    intervals = []
    current = []
    X = sorted(X)
    for i in X:
        if len(current) == 0:
            current = [i, i + 1]
        elif i > current[1]:
            intervals.append(current)
            current = [i, i + 1]
    intervals.append(current)
    return intervals, len(intervals)
