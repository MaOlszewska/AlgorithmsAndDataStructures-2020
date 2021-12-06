'''Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti
dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie
wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane
zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.
'''

'''Sortujemy malejąco po zysku, później szukamy miejsca wolnego dla zadań'''

def profit_of_job(T):
    T.sort( key = lambda x: x[2], reverse = True)
    time = max(T[i][1] for i in range(len(T)))
    time_table = [None for _ in range(time)]
    results = [None for _ in range(time)]
    max_profit = 0

    for i in range(len(T)):
        for j in range(T[i][1] -1, -1, -1):
            if time_table[j] == None and j < len(T):
                time_table[j] = True
                max_profit += T[i][2]
                results[j] = T[i][0]
                break
    res =[]
    for i in range(len(results)):
        if results[i] != None:
            res.append(results[i])
    return max_profit, res
