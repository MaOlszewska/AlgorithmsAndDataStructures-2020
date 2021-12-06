# SORTOWANIE WYRAZÓW O TEJ SAMEJ DLUGOSCI   # O(d( n + k))  k-liczba róznych cyfr , d = liczba cyfr w liczbach,
def radix1(A, n, d):
    for i in range(d-1, -1, -1):
        for j in range(0, n):
            k = 0
            while k + j < n - 1:
                if A[k][i] > A[k + 1][i]:
                    A[k], A[k + 1] = A[k + 1], A[k]
                k += 1
    return A

def counting_sort_digits(A,letter_num):
    k = 2 #mamy tylko dwie litery a i b
    C = [0] * k
    B = [0]*len(A)
    for i in range(len(A)):
        C[ord(A[i][letter_num]) - ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[ord(A[i][letter_num]) - ord('a')] -= 1
        B[C[ord(A[i][letter_num]) - ord('a')]] = A[i]
    return B

def radix_sort(A, k):
    for i in range(k - 1, -1, -1):
        A = counting_sort_digits(A,i)
    return A


# SORTOWAIE WYRAZOW O ROZNEJ DLUGOSCI

def radix(A, n, d):
    for j in range(1, n):
        while j > 0:
            if A[j][d] < A[j - 1][d]:
                A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

def sortstring(A):
    bucket = []
    for i in A:
        while len(i) >= len(bucket):
            bucket.append([])
        bucket[len(i)].append(i)

    for i in range(len(bucket) - 1, 0, -1):
        q = len(bucket[i])
        C = radix(bucket[i], q, i - 1)
        bucket[i - 1] = bucket[i] + bucket[i - 1]
    return C

# SORTOWANIE LICZB
def countingSort(A, x):
    n = len(A)
    output = [0] * n

    count = [0] * 10
    for i in range(0, n):
        index = (A[i] / x)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (A[i] / x)
        output[count[int(index % 10)] - 1] = A[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(A)):
        A[i] = output[i]

def radixdlaliczb(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr

if __name__ == '__main__':
    A = [5,8,10,15,65,76,33,0,234,78,100,567,34,8]
    print(radixdlaliczb(A))