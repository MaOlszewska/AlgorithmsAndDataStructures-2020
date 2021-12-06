class vert:
    def __init__(self):
        self.visited = False
        self.d = -1
        self.low = -1
        self.parent = -1

def DFSb(G, v, nr,vertices):
    vertices[v].visited = True
    nr += 1
    vertices[v].d = vertices[v].low = nr
    for w in G[v]:
        if not vertices[w].visited:
            vertices[w].parent = v
            nr, vertices = DFSb(G, w, nr,vertices)
            vertices[v].low = min(vertices[v].low, vertices[w].low)
            if vertices[w].low == vertices[w].d:
                print((w, vertices[w].parent))
        elif w != vertices[v].parent:
            vertices[v].low = min(vertices[v].low, vertices[w].d)
    return nr, vertices

def bridge(G):
    n = len(G)
    vertices = [vert() for _ in range(n)]
    nr = 0
    for u in range(len(G)):
        if not vertices[u].visited:
           nr, vertices = DFSb(G,u,nr, vertices)

G = [[1,3,7],[0,2],[1,4,3,8],[2,0],[5,6,2],[4,6],[5,4],[0],[8]]
