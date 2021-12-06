from queue import Queue

def cycle(G):
    Q = Queue()
    visited = [False for _ in range(len(G))]
    prev = [None for _ in range(len(G))]
    visited[0] = True
    Q.put(0)

    while not Q.empty():
        s = Q.get()
        for v in G[s]:
            if prev[s] != v and v != s:
                if visited[v] == False:
                    Q.put(v)
                    visited[v] = True
                    prev[v] = s
                else:
                    return True
    return False


def cycle(G):
    Q = Queue()
    color = [None] * len(G)
    prev = [None] * len(G)
    color[0] = True
    Q.put(0)

    while not Q.empty():
        s = Q.get()
        for v in range(len(G)):
            if prev[s] != v and v != s and G[s][v] != 0:
                if color[v] == None:
                    Q.put(v)
                    color[v] = True
                    prev[v] = s
                else:
                    return True
    return False

graf = [[0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0]]
