'''
Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.
'''

'''
Tworzymy graf i Dijkstą szukamy kosztu minimalnego ściezki
'''