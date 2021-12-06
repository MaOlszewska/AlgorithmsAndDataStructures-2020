'''
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który
posortuje tę tablicę w czasie O(n).(Najpierw po dlugosciach, potem leksykograficznie)
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
'''


def countingSort(arr, i):
    letters = ord('z') - ord('a') + 1
    count = [0] * letters
    output = [0] * len(arr)

    for string in arr:
        count[ord(string[i]) - ord('a')] += 1

    for j in range(1, len(count)):
        count[j] += count[j - 1]

    for p in range(len(arr) - 1, -1, -1):
        count[ord(arr[p][i]) - ord('a')] -= 1
        output[count[ord(arr[p][i]) - ord('a')]] = arr[p]

    for i in range(len(arr)):
        arr[i] = output[i]


def radixSort(bucket):
    for i in range(len(bucket[0]) - 1, -1, -1):
        countingSort(bucket, i)

def bucket_string(T):
    for i in range(len(T)):
        T[i] = (T[i], len(T[i]))
    max_lenght = max(T[i][1] for i in range(len(T)))
    bucket = [[] for _ in range(max_lenght + 1)]

    for i in range(len(T)):
        bucket[T[i][1]].append(T[i][0])

    for i in bucket:
        if len(i) > 0:
            radixSort(i)

    T_sorted = []
    for i in bucket:
        T_sorted += i

    return T_sorted

