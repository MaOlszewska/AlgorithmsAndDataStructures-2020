'''
Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
podający kolejność wyłączania stacji.


Dany jest spójny graf nieskierowany G = (V,E). Proszę zaproponować algorytm, który znajdzie taką
kolejność usuwania wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie przestaje
być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie dotykające go krawędzie).
'''

'''usuwamy wierzchołki w takiej kolejnosci w jakiej zostają przetworzone przez BFS'''

from queue import Queue


def delete(G, start):
    Q = Queue()
    visited = [ False for _ in range(len(G))]
    deleted = [start]
    visited[start] = True
    Q.put(start)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.put(v)
                deleted.append(v)
    return deleted

G = [[1,2,3,4],[0,3,4],[0,3,4,5],[0,1,2,4,5], [0,1,2,3,5], [2,3,4]]
print(delete(G, 0))