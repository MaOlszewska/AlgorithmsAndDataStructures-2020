'''
Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami
(wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero)
i zwraca długość (wagę) najdłuższej ścieżki prostej wtym drzewie.
Drzewo reprezentowane jest za pomocą obiektów typu Node
'''

class Node:
    def __init__(self):
        self.children = 0  # ilość dzieci węzła
        self.child = []    # lista par ( dziecko, waga krawędzi
        self.path = 0      # nadłuzsza ścieżka

def heavy_path(T):
    first = 0
    second = 0
    if T.child == None:
        return T.path
    for i in T.child:
        child, weight = i
        curr_lenght = heavy_path(child) + weight
        if curr_lenght > first:
            first, second = curr_lenght,  first
        elif curr_lenght > second:
            second = curr_lenght
    if first + second > T.path:
        T.path = first + second
    return T.path

