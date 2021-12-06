'''
Dane są 3 stringi. Należy stwierdzić, czy ostatni (długości m+n) składa się
z liter pierwszego i drugiego (odpwiednio długości m oraz n).
Kolejność liter w słowach musi zostać zachowana
'''

''' DP[m+1][n+1] - DP[i][j]- czy z i pierwszych liter pierwszego słowa i j liter z drugiego słowa można 
utworzyć i + j liter  z trzeciego słowa. DP[0][0]= True, jeśli DP[i - 1][j] = True to sprawdzamy ze ita 
literaz pierwszego stringa zgadza się z i + j literą trzeciego stringa. Jeśli tak t DD[i][j] = True, jeśli nie to 
sprawdzamy tak samo dla jtej litery drugiego stringa. Jak ani jedna ani druga nie apsuje to ustawiamy wartość
komórki False. Rozwiązanie znajdziemy w komórce DP[m][n]'''

def merge_strings(A, B, C):
    DP = [[None for _ in range(len(A) + 1)] for _ in range(len(B) +1)]
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i == j == 0:
                DP[i][j] = True
            elif DP[i - 1][j] == True and i >= 0:
                if A[i - 1] == C[i + j - 1]:
                    DP[i][j] = True
            elif DP[i][j - 1] == True and j >= 0:
                if B[j - 1] == C[i + j - 1]:
                    DP[i][j] = True
            else:
                DP[i][j] = False
    return DP[len(A)][len(B)]



