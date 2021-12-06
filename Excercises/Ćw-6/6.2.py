'''
Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
[a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
się w całości w tam, który spadł tuż przed nim.
'''

''' DP[i] = ile klocków miescie się na osi liczbowej do itej pozycji'''

def falling_bricks(intervals):
    DP = [1 for _ in range(len(intervals))]
    for i in range(1, len(intervals)):
        for j in range(i):
            if intervals[i][0] >= intervals[j][0] and intervals[j][1] >= intervals[i][1] and DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1
    return len(intervals) - max(DP)
