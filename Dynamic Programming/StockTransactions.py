'''Mając tablice z cenami rpzyszłych akcji, znajdz maksymalny zyzsk uzyskany przez kupno i przedaż n razy akcji
jesli nowa transakcja może rozpoczać sie dopeiro po zakonczeniu poprzedniej, czli w danym czasie możemy posiadać tylko
jedną akcje'''

''' DP[i][j] - maksymalny zysk przy i transakcjach do jtego dnia.
    DP[i][j] = max(DP[i][j - 1], max(price[k] - price[k] + DP[i - 1][k])), gdzie k = 0.... j-1
    DP[i][j-1] ozncacz ze nie wykonaliśmy zadnej transkacji w jtym dniu
    Aby sprzedać akcje w j tym dniu to musimy ją kupić w dowolnym poprzendim, jesli kupimy akcje w ktym dniu i sprzedamy
    w jtym dniu to maksymalny zysk wynsieie price[k] - price[k] + DP[i - 1][k], gdzie k = 0...j-1 i DP[ i -1][k]
    jest najlepszą transkacją do ktego dnia
'''

def max_profit(price, n):
    l = len(price)
    DP = [[None for _ in range(l)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(l):
            if i == 0 or j == 0:
                DP[i][j] = 0
            else:
                Max = 0
                for k in range(j):
                    curr = price[j] - price[k] + DP[i - 1][k]
                    if curr > Max:
                        Max = curr
                DP[i][j] = max(Max, DP[i][j - 1])
    return DP[n][l - 1]


