'''
Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
'''

'''
Wykorzytsamy idee tworzenia kubełków z bucketsorta.
Tworzymy tyle kubełków ile mamy liczb w tablicy. Musimy jeszcze znać liczbę, która bedzie oznaczać połowe z ilosci
pozycji tablicy. Następnie przehcodizmy liniowo po tablicy i każdą liczbę umieszczamy w odpowiednim kubełku. Wrzucamy lizczby do kubełka 
o indeksie n*i/Max, przez co ammy pewnośc, że każa z liczb zostanie umieszczona we właściwym kubełku.
Jeżeli ilość elementów w danym kubełku przekroczy połowe wsyztskich liczb to oznaczy ze ta liczba jest liderem. 
'''
from math import ceil

def bucket_leader(T):
    if len(T) % 2 == 0:
        half = (len(T) / 2) + 1
    else:
        half = ceil(len(T) / 2)

    size = [0 for _ in range(len(T) + 1)]

    Max = max(T)
    for i in T:
        idx = int(len(T) * (i / Max))
        size[idx] += 1
        if size[idx] >= half:
            return True
    return False
# jeśli w kubełku bedzie więcej niż połowa wystąpień jakiejś liczby to znaczy ze jest ona liderem