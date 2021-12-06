''' W wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
przedmiotu pi dane sa nastepujace trzy liczby:
1. v(pi) – wartość przedmiotu,
2. w(pi) – waga przedmiotu, oraz 3.
3. h(pi) – wysokość przedmiotu.
Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
jego poprawność'''

def knapsack(W, H, P, MaxW, MaxH):
   n = len(P)
   F = [[[0] * (MaxH + 1) for _ in range(MaxW + 1)] for _ in range(n)]
   for w in range(W[0], MaxW + 1):
       for h in range(H[0], MaxH + 1):
           F[0][w][h] = P[0]

   for i in range(1, n):
       for w in range(1, MaxW + 1):
           for h in range(1, MaxH + 1):
               F[i][w][h] = F[i - 1][w][h]
               if w >= W[i] and h >= H[i]:
                   F[i][w][h] = max(F[i][w][h], F[i - 1][w - W[i]][h - H[i]] + P[i])
   return F[n - 1][MaxW][MaxH], F


def getsolution(F, W, H, P, i, w, h):
   if i == 0:
       if w >= W[0] and h >= H[0]:
           return [0]
       return []
   if w >= W[i] and h >= H[i] and F[i][w][h] == F[i - 1][w - W[i]][h - H[i]] + P[i]:
       return getsolution(F, W, H, P, i - 1, w - W[i], h - H[i]) + [i]
   return getsolution(F, W, H, P, i - 1, w, h)