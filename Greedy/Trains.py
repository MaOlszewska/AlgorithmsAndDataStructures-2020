'''
Biorąc pod uwagę godziny przyjazdu i odjazdu wszystkich pociągów, które docierają na stację kolejową,
zadaniem jest znalezienie minimalnej liczby peronów wymaganych dla stacji kolejowej, aby żaden pociąg nie czekał.
'''

'''
Sortujemy pociągi po godzinie przyjazdu rosnąco i po godzinie odjazdu, sprawdzamy dla koljenych pociagów
czy ich czas przyjazdu jest wiekszy lub rówy czasowi odjazdu poprzedniego
Jeśli nie to znaczy ze musimy dodać koeljny peron
'''

def trains(t):
    departure = [t[i][1] for i in range(len(t))]   # wyjazdy
    arrival = [t[i][0] for i in range(len(t))]     # przyjazdy

    departure.sort()
    arrival.sort()
    platforms = 1
    platforms_curr = 1
    i = 1
    j = 0
    while i < len(t) and j < len(t):
        if arrival[i] <= departure[j]:
            i += 1
            platforms_curr += 1
        elif arrival[i] > departure[j]:
            j += 1
            platforms_curr -= 1
        if platforms_curr > platforms:
            platforms = platforms_curr
    return platforms

T = [[1,5], [2,4], [3,7], [4,5], [6,7], [2,4], [5,9]]
print(trains(T))