class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 1
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(G,K):
    n = len(G)
    edges = []
    G.sort(key = lambda G: G[2])

    for i in range(n):
        edges.append(Node(i))

    A = []
    weight = 0
    for edge in range(n):
        v = edges[G[edge][0]]
        u = edges[G[edge][1]]
        if not find(v) is find(u) and G[edge][2] < K: # czy v i u leżą w innych składowych grafu
            union(v, u) # łaczymy zbiory
            A.append((v.val, u.val))
            weight += G[edge][2]
    count = 0
    print(A)
    for i in range(1, len(A)):    # to Chyba przypadek, że to działa
        if find(edges[A[i][0]]) is not find(edges[A[i-1][0]]):
            print(A[i][0], A[i][1] )
            count += 1
    print(count)
    return weight, A, count

def lotniska(G, K):
    W, A, count = kruskal(G, K)
    return W + count * K



G = [(0,1,5),(0,2,4), (0,6,6),(1,5,2),(2,3,2),(2,4,7),(6,4,3), (5,4,5),(3,4,6)]

print(lotniska(G, 5))