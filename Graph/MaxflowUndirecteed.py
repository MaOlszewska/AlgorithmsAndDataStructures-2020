from queue import Queue
def BFS(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)

    visited[s] = True
    distance[s] = 0

    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)

    return visited[t]


def Ford_Fulkerson(G, s, t):
    n = len(G)
    parents = [None] * n
    flow = 0
    while BFS(G, s, t, parents):
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parents[current]][current] < cur_flow:
                cur_flow = G[parents[current]][current]
            current = parents[current]
        flow += cur_flow
        v = t
        while (v != s):
            G[parents[v]][v] -= cur_flow
            G[v][parents[v]] += cur_flow
            v = parents[v]
    return flow

def MaxFlowUndirected(G):
    n = len(G)
    E = 0
    for u in range(len(G)):
        for v in range(u, len(G)):
            if G[u][v] != 0:
                E += 1
    directedG = [[ 0 for _ in range(n + E)] for _ in range(n + E)]

    curr = n
    for u in range(n):
        for v in range(u, n):
            if G[u][v] != 0:
                directedG[u][v] = G[u][v]
                directedG[v][curr] = G[u][v]
                directedG[curr][u] = G[u][v]
                curr += 1
    return Ford_Fulkerson(directedG, 0, 4)


G = [[0, 4, 3, 3, 0],
     [4, 0, 7, 0, 0],
     [3, 7, 0, 4, 2],
     [3, 0, 4, 0, 5],
     [0, 0, 2, 5, 0]]

print(MaxFlowUndirected(G))