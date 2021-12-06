def DFS(graph, visited, n, v, v_start, cycle, paths):
    visited[v] = True
    if n == 0:
        visited[v] = False
        if v in graph[v_start]:
            paths.append(cycle)
            return paths
        else:
            return paths
    for i in G[v]:
        if visited[i] == False:
            next_cycle = cycle[:]
            next_cycle.append(i)
            paths = DFS(graph, visited, n - 1, i, v_start, next_cycle, paths)
    visited[v] = False
    return paths

def countCycles( G):
    n = 4
    visited = [False for _ in range(len(G))]
    paths = []
    for v in range(len(G) - (n - 1)):
        paths = DFS(G, visited, n - 1, v, v, [v], paths)
        visited[v] = True
    return paths
G = [[1,3], [0,2,4], [1,3], [0,2,4], [1,3]]

###########################################################################################

def DFS1(graph, visited, n, v, v_start, cycle, paths):
    visited[v] = True
    if n == 0:
        visited[v] = False
        if v in graph[v_start]:
            paths = cycle
            return cycle, paths
        else:
            return cycle, paths
    for i in G[v]:
        if visited[i] == False:
            next_cycle = cycle
            cycle, paths= DFS1(graph, visited, n - 1, i, v_start, cycle + [i], paths)
            if len(paths) > 1:
                break
            else:
                cycle = next_cycle
    visited[v] = False
    return cycle, paths
def countCycles( G):
    n = 4
    visited = [False for _ in range(len(G))]
    paths = []
    for v in range(len(G) - (n - 1)):
        cycle, paths = DFS1(G, visited, n - 1, v, v, [v], paths)
        visited[v] = True
        if paths:
            break
    return paths
G = [[1,3], [0,2,4], [1,3], [0,2,4], [1,3]]


