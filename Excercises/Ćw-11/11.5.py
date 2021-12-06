'''
Formuły logiczne z dwoma wystąpieniami zmiennej) Dana jest formuła logiczna
postaci: C1 ∧ C2 ∧ ⋯ ∧ Cm, gdzie każda Ci to klauzula będąca alternatywą zmiennych i/lub ich zaprzeczeń.
Wiadomo, że każda zmienna występuje w formule dokładnie dwa razy, raz zanegowana i raz niezanegowana.
Na przykład poniższa formuła stanowi dopuszczalne wejście:
(x ∨ y ∨ z) ∧ (y ∨ w) ∧ (z ∨ v) ∧ (x ∨ w) ∧ (v).
Proszę podać algorytm, który oblicza takie wartości zmiennych, że formuła jest prawdziwa.
'''

'''
Stworzenie grafu dwudzielne, gdzie po jednej stronie by były zmienne, a po drugiej formuły logiczne.
wystarczy znaleźć maksymalne skojarzenie.
'''