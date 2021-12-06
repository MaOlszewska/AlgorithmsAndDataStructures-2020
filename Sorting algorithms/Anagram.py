'''Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
alfabetem długości k, sprawdza czy A i B są swoimi anagramami.'''

def anagram(A, B, k):
    if len(A) != len(B):
        return False
    letters = [0 for _ in range(2 ** 16)]

    for i in range(len(A)):
        letters[ord(A[i])] += 1
        letters[ord(B[i])] -= 1

    for i in range(len(A)):
        if letters[ord(A[i])] != 0 or letters[ord(B[i])]:
            return False
    return True
