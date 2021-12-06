'''Mamy podane wysokosci n wież i wartoś k. Musimy albo zminiejszyć albo zwikszyć wysokość każdej wieży
o k . Należy zminimalizować różnice między wysokoscia najwyższej i najniższej wieży po modyfikacji'''

'''SOrtujemy tablice, początkowo naszą róznicą jest wysoksoć z indeksu zero i ostatniego.
Następnie dla każdej wieżyy od lewej strony zwikszamy jej wysokośc o k, a z lewej zmiejszamy o k
'''
def diff(T, k):
    n = len(T)
    T.sort()
    minimized = T[n - 1] - T[0]

    for i in range(1, n):
        smallest = min(T[0] + k, T[i] - k)
        tallest = max(T[i - 1] + k, T[n - 1] - k)
        minimized = min(minimized, tallest - smallest)

    return minimized
T = [1, 10, 14, 14, 14, 15]
k=6

print(diff(T, k))
