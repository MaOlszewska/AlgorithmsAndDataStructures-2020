'''Mając pręt długości n i liste cen częsci o długości i  (1 <= i <= n), znajdź sposób na pocięcie pręta
na mniejszę częscie o najwikeszym zysku'''

def RodCutting(n, price):
    if n == 0:
        return 0
    MaxCost = -1
    for i in range(1, n + 1):
        cost = price[i - 1] + RodCutting(price, n - 1)
        if cost > MaxCost:
            MaxCost = cost
    return MaxCost

def cut_rod(price,n):
    DP=[0]*(n+1)
    DP[1] = price[1]

    for length in range(2,n+1) :
        for j in range(1,length+1) :
            DP[length] = max(DP[length], price[j] + DP[length-j])
    return DP[n]