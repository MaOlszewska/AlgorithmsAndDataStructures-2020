'''
Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który
znajduje takie dwie liczby x i y z A, że y −x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej,
że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla
których A[i + 1] − A[i] jest największe).
'''

'''
Korzystamy z idei bucketów, Tworzymy tyle kubelków ile jest liczb w tablicy. Każdą liczbę wkładamy do odpowiedniego 
kubełka. Nastepnie sortujemy te liczby w kubełkach rosnaco. Przechodizmy liniowo po tablicy z kubełakmi i sprawdzamy różnice 
z sąsiednich kubełków. Z poprzedniego bbierzemy max a z nastepnego min. Róznica ta ma być maxymalna-wynik.
Jesli będizmey brać zawsze skrajne liczby z kubelków wtedy mamy pewnośc, że pomiedzy tymi liczbami nie ma żadnych innych,
wiec warunki zadania są spełnione.
'''


def maxpair(T):
    n = len(T)
    Max = T[0]
    Min = T[0]
    for i in range(n):
        Max = max(Max, T[i])
        Min = min(Min, T[i])

    buckets = [[] for _ in range(n)]
    x = (Max + Min) / n

    for i in range(n):
        idx = int((T[i] - Min) / x)
        buckets[idx].append(T[i])
    result = 0
    prevMax = max(buckets[0])

    for i in range(1, n):
        if len(buckets[i]) != 0:
            currMin = min(buckets[i])
            result = max(result, currMin - prevMax)
            prevMax = max(buckets[i])

    return result
