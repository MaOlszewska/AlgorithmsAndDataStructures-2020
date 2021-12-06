'''
Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A
do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A
jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
(1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
(2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa).
 Na każdej stacji możemy tankować dowolną ilość paliwa.
(3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna
'''

#1
def tank_fueling1(distance, fuel, stations):
    fuel_limit = fuel
    curr_pos = 0
    stops = 0
    while fuel_limit < distance:
        while stations[curr_pos] <= fuel_limit and curr_pos < len(stations) - 1:
            curr_pos += 1
        stops += 1
        fuel_limit = stops[curr_pos] + fuel
        curr_pos += 1
    return stops

def tank(S, L, d):  #?
    S = [0] + S + [d]
    fuel = L
    stops  = 0
    for i in range(1, len(S)):
        distance = S[i] - S[i - 1]
        if distance > fuel:
            stops += 1
            fuel = L - distance
        else:
            fuel-= distance
    return stops


