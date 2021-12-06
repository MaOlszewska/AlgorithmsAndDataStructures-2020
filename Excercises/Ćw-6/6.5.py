'''
Proszę zaproponować algorytm dla dwuwymiarowej
wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
przedmiotu pi dane sa nastepujace trzy liczby:
1. v(pi) – wartość przedmiotu,
2. w(pi) – waga przedmiotu, oraz
3. h(pi) – wysokość przedmiotu.
Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
jego poprawność.
'''
'''
DP[i][w][h] = Najwieksz zysk jaki mozna osiągnąc wybierajac przedmioty od 0 do i nie przekraczjac wagi w i
wysokości h
'''
def knapsack(W, H, P, MaxW, MaxH):
    n = len(W)
    DP = [[[0 for _ in range(MaxH + 1)] for _ in range(MaxW + 1)] for _ in range(n)]
    for w in range(MaxW + 1):
        for h in range(MaxH + 1):
            DP[0][w][h] = P[0]
    for i in range(1, n):
        for w in range(1, MaxW + 1):
            for h in range(1, MaxH + 1):
                DP[i][w][h] = DP[i-1][w][h]
                if w >= W[i] and h >= H[i]:
                    DP[i][w][h] = max(DP[i][w][h], DP[i - 1][w - W[i]][h - H[i]] + P[i])
    return DP

def getsolution(F, W, H, P, i, w, h):
   if i == 0:
       if w >= W[0] and h >= H[0]:
           return [0]
       return []
   if w >= W[i] and h >= H[i] and F[i][w][h] == F[i - 1][w - W[i]][h - H[i]] + P[i]:
       return getsolution(F, W, H, P, i - 1, w - W[i], h - H[i]) + [i]
   return getsolution(F, W, H, P, i - 1, w, h)

P = [3,5,1,2,1,5]
W = [1,2,4,3,2,1]
H = [2,1,4,3,1,3]

result = knapsack(W,H,P,7,10)
print(result[len(P) - 1][7][10])
print(getsolution(result, W, H, P,len(P) -1 , 7, 10))