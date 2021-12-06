'''
Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
'''

'''
Zamieniamy na odpowiadajęce liczby w kodzie ASCII, przechodizmy liniowo po słowie A i B,
dodajac do tablicy na odpowiednim miejscu jedynkę jeżeli dana litera wystepuje w słowie A i odejmujemy jedynke jeżeli
litera wystęepuje w słowie B. Pózniej sprawdzamy czy wsyztskie pozycje w tablicy z literami równaja się zero.
Jeśli nie to słwoa nie są anagramami.
'''

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