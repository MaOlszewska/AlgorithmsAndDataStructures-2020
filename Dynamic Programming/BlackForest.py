def BlackForest(cost):
    DP = [0 for _ in range(len(cost))]
    DP[0] = cost[0]
    DP[1] = max(cost[0], cost[1])

    for i in range(2, len(cost)):
        DP[i] = max(DP[i - 2] + cost[i], DP[i - 1])

    return DP[len(cost) - 1]

T = [6,1,2,3,4,7,1,2,3]
print(BlackForest(T))