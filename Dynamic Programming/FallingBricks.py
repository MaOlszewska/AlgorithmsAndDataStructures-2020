'''
Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim.
'''

def bricks(T):
    DP = [1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if T[i][0] >= T[j][0] and T[j][1] >= T[i][1] and DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1
    return len(T) - max(DP)
