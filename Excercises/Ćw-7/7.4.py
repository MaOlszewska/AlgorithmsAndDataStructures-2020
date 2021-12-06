'''
Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków
o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
(ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
jednego ładunku, to lepsze jest to pierwsze rozwiązanie).
'''

'''
Sortujemy ładunki w kolejności malejącej, nastepnie przechodizmy po tablicy z ładunkami i sprawdzamy
czy dany ładunek zmieście się jeszcze w przyczepie jesli tak to zwiekszamy licznik ładunków
i odejmujemy od pojemonosci masę tego łądunku.
'''

def trailer(K, W):
    W.sort(reverse = True) # sortowanie malejąco
    count = 0
    CpK = K
    for i in range(len(W)):
        if K - W[i] >= 0:
            count += 1
            K -= W[i]
    return count, CpK - K