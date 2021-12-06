'''
Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
wychodząca z t.
'''

'''
W reprezentacji macierzowej jeśli wierzchołek jest universalnym ujsciem to w całym sowim wierszu musi mieć zera,(bo nie moze
wychodzić z niego zadna krawęz do innego wierzchołka),
a w kolumnie jedynki.(Bo wszytskie wierzhcołki muszą być skierowane do wierzchola v.
Kiedy napotkamy na wartość 0 idziemy "w prawo" (inkrementujemy v), jeżeli na 1, to "w dół".
Kiedy dojdziemy z v poza ostatnią kolumnę, oznacza to tyle, że wierzchołek u 
jest kandydatem - i tylko dla niego sprawdzamy, czy cały u-ty wiersz składa się z 0, 
a cała u-ta kolumna z 1 (z wyjątkiem u-tego elementu). Jeżeli natomiast wyjdziemy z v za
ostatni wiersz, to ujścia nie ma.
'''
def universalSink(g):
    i = 0
    j = 0
    n = len(g)
    while i < n and j < n:
        if g[i][j] == 1:
            i += 1
        else:
            j += 1

    if j == n - 1:
        return False

    for k in range(n):
        if g[i][k] != 0:
            return False
        if g[k][i] != 1 and i != k:
            return False

    return i

