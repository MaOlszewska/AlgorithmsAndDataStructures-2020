'''
Dana jest posortowana tablica A zawierająca n liczb i celem jest wyznaczenie liczby x takiej, że wartość
 ∑n−1 i=0 ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić
jego poprawność oraz ocenić złożoność obliczeniową.
'''

def min_sum(T, n): # x bedzie mediana
   T.sort()
   x = T[n // 2]
   sum = 0
   for i in range(n):
       sum += abs(T[i] - x)
   return sum