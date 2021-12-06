'''
Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.
'''
from math import ceil


def bucket_leader(T):
    if len(T) % 2 == 0:
        half = (len(T) / 2) +1
    else:
        half = ceil(len(T) / 2)

    buckets = [[] for _ in range(len(T) + 1)]
    size = [0 for _ in range(len(T) + 1)]

    Max = max(T)
    for i in T:
        idx = int(len(T) * (i / Max))
        buckets[idx].append(i)
        size[idx] += 1
        if size[idx] >= half:
            return True
    return False

# jeśli w kubełku bedzie wiećej niż połowa wyśtpaień jakiejś liczby to znaczy ze jest ona liderem
