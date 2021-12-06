'''
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
 Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.
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


def zbigniew(A):
    energy = sum(A)
    n = len(A)
    DP = [[float('inf') for _ in range(energy + 1)] for _ in range(n)]
    DP[0][A[0]] = 0

    for i in range(n):  # pozycje na których jest zbigniew
        for j in range(energy):  # ile ma zbigniew energi
            if DP[i][j] != float('inf'):
                jump = i + 1
                while jump < n and j >= jump - i:  # na ile zkoków starczy zbigniewowi energii
                    DP[jump][j - jump + i + A[jump]] = min(DP[jump][j - jump + i + A[jump]], DP[i][j] + 1)
                    jump += 1
    return min(DP[n - 1])
