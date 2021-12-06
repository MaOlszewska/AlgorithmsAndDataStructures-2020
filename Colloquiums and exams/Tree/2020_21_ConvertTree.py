'''
Drzewo BST T reprezentowane jest przez obiekty klasy Node:
    class Node:
        def __init__(self):
            self.left = None    # lewe poddrzewo
            self.right = None   # prawe poddrewo
            self.parent = None  # rodzic drzewa jeśli isnieje
            self.value = None   # przechowywana wartosc

Proszę zaimplementowac funckje:
    ConvertTree(T):
która przekształca drzewo T na drzewo o minimalnej wysokości, w którym węzły spełniają warunek:
największy element na danym poziomie jest mniejszy od najmniejszego elementu na kolejnym poziomie.
Funkcja zwraca korzen nowego drzewa. Poziomy numerjemy od korzenia do liści.
'''


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrewo
        self.parent = None  # rodzic drzewa jeśli isnieje
        self.value = None  # przechowywana wartosc


