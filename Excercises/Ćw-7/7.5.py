'''
Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko
ma klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach w
, itd. Dzieci właśnie poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko
zostało. Ma teraz jedyną okazję, żeby podebrać kilka klocków innym dzieciom tak, żeby jego wieża była
najwyższa. Proszę podać możliwie najszybszy algorytm rozwiązujący ten problem, który zabiera minimalną
ilość klocków. (Proszę zwrócić uwagę, że liczby w i j mogą być bardzo duże.)
'''

'''
W tablicy zapisujemy sume wysokosci klocków każdego z dzieci i sortujemy ich klocki po wysokosci rosnąco.
Nastepnie obliczamy wysokość dopóki jetest ona mniejsza od maksymalnej sumy wysokosci klocków.
Do wysokosci dodajemy najwyzszy klocek od dziecka z najwyższą wieżą i suwamy tenże klocek z klocków tego dziecka.
pamiętając o tym, żeby zmienić sume i zwiekszyć licznik.
'''
def tower(T):
    sumy = []
    for i in range(len(T)):
        sumy.append(sum(T[i]))
        T[i].sort()

    count = 0
    curr_height = 0
    while curr_height < max(sumy):
        count += 1
        idx = sumy.index(max(sumy))
        heigh = T[idx].pop()
        curr_height += heigh
        sumy[idx] -= heigh

    return count