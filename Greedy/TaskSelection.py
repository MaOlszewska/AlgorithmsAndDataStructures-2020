'''
    Dana jest tablica z godzinami rozpoczecia i zakonczenia danej czynnnosći.Nalęzy wybrać maksymalną liczbę
    czynnosci które może ywkonać jedna osoba, zakłądająć ze nie może wykonywac kilku czynnosci w jednakowym czasie
'''

'''
    Nalezy posortoać czynnosci wzgledem czasu ich zakonczenia, wybieramy pierwszą czynnosći jako pierwszą
    w tablicy, aby wybrać kolejne należy sprawdzić czy czas rozpoczęcia kolejnej czynnnosci jest większy lub
    równy czasowi zakonczenia poprzednio wybranej czynnosci
'''

T = [['a', 5, 9], ['b', 1, 2], ['c', 3, 4], ['d', 0, 6], ['e', 5, 7], ['f', 8, 9]]
def selection(t):
    t.sort(key=lambda x: x[2])
    task = [T[0][0]]
    prev = 0
    for i in range(1, len(t)):
        if t[i][1] >= t[prev][2]:
            task.append(T[i][0])
            prev = i
    return task
