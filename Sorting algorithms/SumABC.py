'''
    Dane są trzy zbiory: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c
    z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!
'''

def sumABC(A, B, C):
    A = sorted(A)
    B = sorted(B)

    for i in C:
        left = 0
        right = len(B) - 1
        while left < len(A) and right >= 0:
            if A[left] + B[right] == i:
                return True
            elif A[left] + B[right] < i:
                left += 1
            else:
                right -= 1
    return False
