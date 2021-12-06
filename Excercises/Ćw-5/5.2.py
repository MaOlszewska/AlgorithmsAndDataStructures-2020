'''
Dana jest tablica n liczb A. Proszę podać i zaimplementować algorytm, który sprawdza, czy da się wybrać
podciąg liczb z A, które sumują się do zadanej wartości T.
'''

# f(i, s) - czy z liczb a[1] od zera do a[i] da sie otrzymac sume s
# f(n, T)

# f(i, s) = f(i - 1, s) lub f(i-1, s-a[i]) pod warunkiem, ze s - a[i] > 0
# f(0, 0) - prawda
# f(0, s) - falsz dla s > 0

'''
W wierszach mamy sumy od 0 do t, a w kolumanch długości przedziałow od 0.
całą pierwszą kolumnę ustawiamy na 0, bo bo z zera elementów nie możemy utorzyć żadnej sumy, 
a cały pierwszy wiersz usatwiamy na 1, boo możmey utworzyc sume rowną 0 nie biorąc poprostu żadnej z liczb.
jesli wartosc ostatniego elementu z danego przedzialu jest wieksza od sumy ktora chcemy uzyskac, to wiem ze jej nie moge wziac.
jezeli ten element moze sie zmiescic do sumy, to sprawdzam czy te sume dalo sie utworzyc uzywajac wczesniejszych elementow,
tzn ze teraz takze da sie ja utworzyc. Natomiast jezeli wczesniej nie dalo sie, to sprawdzam czy za pomoca wczesniejszyc jestem
w stanie utworzyc sume pomniejszona o wartosc tego aktualnego elementu, wystarczy nam jedna z tych mozliwosci.
'''

def subsetsum(T, target):
    n = len(T)
    DP = [[0 for _ in range(n + 1)] for _ in range(target + 1)]
    for i in range(target + 1):
        DP[i][0] = 0
    for i in range(n + 1):
        DP[0][i] = 1
    for sum in range(1, target + 1):
        for lenght in range(1, n + 1):
            if T[lenght - 1] > sum:
                DP[sum][lenght] = DP[sum][lenght - 1]
            else:
                DP[sum][lenght] = (DP[sum][lenght - 1] or DP[sum - T[lenght - 1]][lenght - 1])
    if DP[target][n] == 1:
        return True
    return False