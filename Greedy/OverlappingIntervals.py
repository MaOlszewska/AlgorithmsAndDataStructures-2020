'''
Mając zestaw N przedziałów czasowych,zadaniem jest znalezienie przedziałów,
 które nie pokrywają się z podanym zestawem przedziałów.
'''

'''Należy posortować rosnąco przedziały według czasu rozpoczęcia, sprawdzić jeden po drugim czy się nie nakładają
jeślei się nie nakłądają to mamy jeden z suzkanych przedziałow o początku w końcu pierwszego i końcu w początku drugiego
jeśli się nakłądają to sprawdzamy kolejne 
:)
'''

def overlapping_intervals(T):
    T.sort(key = lambda x: x[0])
    n = len(T)
    intervals = []
    for i in range(1, n):
        if T[i][0] > T[i - 1][1]:
            intervals.append([T[i - 1][1], T[i][0]])
    return intervals
