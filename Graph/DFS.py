class VertexRaw:   # Klasa przechowująca informacje o wierzchołkach
    def __init__(self):
        self.visited = False  # czy był już odwiedzony
        self.parent = None  # kto jest jego rodzicem

def DFSVisit(G, vertices, u, path):
    vertices[u].visited = True
    for v in G[u]:
        if not vertices[v].visited:
            vertices[v].parent = u
            DFSVisit(G, vertices, v, path)
    path.insert(0,u)
def Dfs(G):
    n = len(G)
    vertices = []
    result = []
    for _ in range(n):
        vertices.append(VertexRaw())
    for v in range(n):
        if not vertices[v].visited:
            DFSVisit(G, vertices, v, result)
    return result

#######################################################################

def DFS_visit(G, u, visited, path):
    visited[u] = True
    for v in G[u]:
        if visited[v] == False:
            DFS_visit(G, v, visited, path)
    path.insert(0,u)

def DFS(G):
    visited = [False for _ in range(len(G))]
    path = []
    for u in range(len(G)):
        if visited[u] == False:
            DFS_visit(G, u, visited, path)
    return path

def DFSmatrix(G):
    visited = [False for _ in range(len(G))]
    path = []
    for u in range(len(G)):
        if visited[u] == False:
            DFS_visit(G, u, visited, path)
    return path


def DFS_visit_matrix(G, u, visited, path):
    visited[u] = True
    for v in range(len(G)):
        if visited[v] == False and G[u][v] != 0:
            DFS_visit(G, v, visited, path)
    path.insert(0,u)

G = [[3], [3,4,5], [4], [0,1,4,5], [2,1,3,5],[3,4,1]]
