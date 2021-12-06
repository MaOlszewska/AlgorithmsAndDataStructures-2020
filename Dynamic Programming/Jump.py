'''
dana jest tablica T zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji 0;
wartość T[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję. Przykład T=[1,3,2,1,0].
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile
sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
'''

'''DP[i] - ilośc sposóbów na dotarcie do pocyzji n -1 z itego indeksu.
DP[n-2] = 1 to jest pewne, pozniej cofamy się do mniejszych indeksów i sumujemy liczbe mozliscosci skoków o długosci 1-max
-DP[ i + len], którą juz mamy policzoną , jesli da się skoczyć z i na n -1 odrazu to dodajemy jedną możliwość
'''

def jump(T):
    DP = [0 for _ in range(len(T))]
    DP[len(T) - 2] = 1

    for i in range(len(T) - 3, -1 , -1):
        Max = T[i] # długośc skoku z pozycjii i
        for j in range(1, Max + 1):
            if i + j == len(T) - 1:
                DP[i] += 1
                break
            else:
                DP[i] = DP[i + j]

    return DP[0]