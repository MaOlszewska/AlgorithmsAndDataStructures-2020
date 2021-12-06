def knapsack(W, P, MaxW):
    n = len(W)
    DP = [[0 for _ in range(MaxW + 1)] for _ in range(n)]
    for w in range(0, MaxW + 1):
        DP[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, MaxW + 1):
            DP[i][w] = DP[i-1][w]
            if w >= W[i]:
                DP[i][w] = max(DP[i][w], DP[i - 1][w - W[i]] + P[i])
    return DP[n - 1][MaxW]


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
knapsack(W, P, 16)