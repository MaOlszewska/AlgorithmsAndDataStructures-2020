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
# 1
''' 
Algorytm zachłanny w którym jedziemy najdaej tam gdzie nam wysarcza paliwa. 
Jeżeli nie jeseśmy w stanie dojechac na następną stacje to tankujemy na tej na której jeśteśmy.
Algorytm jest poprawny daltego, że nie bedziemy zatrzymywac bez potrzeby, tylko wtedy keidy bedziemy musieli,
więc liczba tankowań jest minimalna'''

def tank_fueling(tank, distance, stations):
    actual_fuel = tank
    petrol_station = []
    curr_position = 0

    while actual_fuel < distance:
        if curr_position >= len(stations) or stations[curr_position] > actual_fuel:
            return False
        while curr_position < len(stations) - 1 and stations[curr_position + 1] <= actual_fuel:
            curr_position += 1
        actual_fuel = stations[curr_position] + tank
        petrol_station.append(curr_position)
        curr_position += 1

    return petrol_station

S = [3, 7, 11, 15, 18, 20, 24, 29, 31, 33, 36, 42]
tank = 8
distance = 45

print(tank_fueling(10,distance, S))

