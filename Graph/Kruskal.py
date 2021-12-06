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

def kruskal(G):
    n = len(G)
    edges = []
    t = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                t.append((G[i][j], i, j))
    t.sort(key = lambda t: t[0])

    for i in range(n):
        edges.append(Node(i))

    A = []
    weight = 0
    for edge in range(n):
        v = edges[t[edge][1]]
        u = edges[t[edge][2]]
        if not find(v) is find(u): # czy v i u leżą w innych składowych grafu
            union(v, u) # łaczymy zbiory
            A.append((v.val, u.val))
            weight += t[edge][0]
    return weight, A

G =[[0,2,7,8,0,3],
    [2,0,0,0,5,0],
    [7,0,0,1,0,0],
    [8,0,1,0,4,12],
    [0,5,0,4,0,5],
    [3,0,0,12,6,0]]
