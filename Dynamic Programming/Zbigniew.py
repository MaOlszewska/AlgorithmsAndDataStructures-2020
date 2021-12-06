'''
Zadanie 4. (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc
wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i) kosztuje ją j − i jednostek energii, a
jej energia nigdy nie może spaść poniżej zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na
niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej (wartość przekąki
dodaje się do aktualnej energii Zbigniewa). Proszę zaproponować algorytm, który oblicza minimalną liczbę
skoków potrzebną na dotarcie z 0 do n − 1 majać daną tablicę A z wartościami energetycznymi przekąsek na
każdej z liczb.
'''

def hungryFrog( A ):
    n = len(A)
    allEnergy = sum(A)
    DP = [[float('inf') for _ in range(allEnergy + 1)] for _ in range(n)]
    DP[0][A[0]] = 0

    for currpoz in range(n):
        for energy in range(allEnergy):
            if DP[currpoz][energy] != float('inf'):
                jump = currpoz + 1
                while jump < n and energy >= jump - currpoz:
                    DP[jump][energy - jump + currpoz + A[jump]] = min(DP[jump][energy - jump + currpoz + A[jump]], DP[currpoz][energy] + 1)
                    jump += 1

    return min(DP[n-1])