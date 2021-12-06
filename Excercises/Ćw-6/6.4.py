'''
Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb.
'''

'''
DP[i][j] = minimalna lizcba skoków potrzebna na dotarcie do pola i mając j energii po skoku
        _  _
       (.)(.)
   ,-.(.____.),-.  
  ( \ \ '--' / / )
   \ \ / ,. \ / /
    ) '| || |' ( 
OoO'- OoO''OoO -'OoO
'''

def zbigniew_frog(snacks, n):
    energy = sum(snacks)
    DP = [[float('inf') for _ in range(energy + 1)] for _ in range(n)]
    DP[0][snacks[0]] = 0

    for i in range(n):  # pozycje na których jest zbigniew
        for j in range(energy): # ile ma zbigniew energi
            if DP[i][j] != float('inf'):
                jump = i + 1
                while jump < n and j >= jump - i:  # na ile zkoków starczy zbigniewowi energii
                    DP[jump][j - jump + i + snacks[jump]] = min(DP[jump][j - jump + i + snacks[jump]], DP[i][j] + 1)
                    jump += 1
    return min(DP[n - 1])

