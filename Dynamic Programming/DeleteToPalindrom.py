'''Mając dany ciąg, należy znaleźć minimalną liczbę  usunieć wymaganacyh do przekształcenia go w palindrom'''

'''Należy porównywać ostatni znak ciągu S[i...j] z pierwszym,
Jesli ostatni znak ciągu jest taki sam jak pierwszy to nie koniecznie trzeba usuwać więc powtarzamy dla ciagu S[i=1,j-1]
Jesli ostatni się różni to wybieramy minimum z S[i, j -1], S[i+1, j]
'''

def delete(S, i, j):
    if i >= j:
        return 0
    if S[i] == S[j]:
        return delete(S, i +1, j - 1)
    return 1 + min(delete(S, i, j - 1), delete(S, i + 1, j))
