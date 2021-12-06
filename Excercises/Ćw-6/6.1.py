'''
Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci, jaki
można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
John znajdzie optymalny plan wycinki.
'''

'DP[i] = maksymalny zysk jaki można uzyskac wybierajac drzewa do sciecia od pozycji 0 do i.'
'DP[n - 1] - Tu znajdziemy wynik'
'DP[0] = profits[0]'
'DP[1] = max(profits[1], DP[0])'
'DP[i] = max(DP[i-1], DP[i - 2] + profits[i]) '

def black_forest(n, profits):
    DP = [0 for _ in range(n)]
    DP[0] = profits[0]
    DP[1] = max(profits[1], profits[0])

    for i in range(2, n):
        DP[i] = max(DP[i - 1], DP[i - 2] + profits[i])
    return DP[n - 1]
