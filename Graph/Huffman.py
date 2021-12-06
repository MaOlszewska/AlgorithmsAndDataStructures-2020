#POŻYCZONE

# złozonosc optymistyczna nlogn a pesymistyczna przy złym rozłozeniu drzewa n^2

from queue import PriorityQueue

S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]


class Node:  # tworzymy klase drzewa
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.letter = letter

    # funkcje do porownywania nodów bo bez nich priority queue porównuje drugi element tupla a nie może
    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


def huffman(S, F):
    q = PriorityQueue()  # tworzymy kolejke priortetową

    for i in range(len(F)):
        q.put((F[i], Node(F[i], S[
            i])))  # wypełniamy kolejkę tuplami o polu równym wartości oraz polu równym wskaźnikowi na Node utworzonego dla każdej litery

    while (q.qsize() != 1):  # laczymy 2 konce w jeden dopóki nie pozostanie nam tylko 1
        first = q.get(0)
        second = q.get(1)
        # print("merging:  ", first, "   ", second)
        parent = Node(first[0] + second[0], first[1].letter + second[1].letter, first[1],
                      second[1])  # tworzymy nowego parenta z wczesniejszych nodów
        q.put((parent.value, parent))  # dodajemy parenta do kolejki priorytetowej

    how_many_b_for_writting = 0
    for i in range(len(S)):
        letter = S[i]
        curr = parent
        tmp_bin = ""
        while curr.left or curr.right:  # dopóki istnieją dzieci
            if letter in curr.left.letter:  # przemieszczamy się w dół drzewa w poszukiwaniu dzieci zawierajacych szukaną przez nas literę
                tmp_bin += "0"
                curr = curr.left
            else:
                tmp_bin += "1"
                curr = curr.right

        how_many_b_for_writting += len(tmp_bin) * F[i]  # obliczamy liczbe bitow potrzebna do zapisu napisu
        print(letter, " :  ", tmp_bin)

    print("dlugosc napisu:  ", how_many_b_for_writting)


# S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "r", "s", "t", "u", "w", "y", "z", "q"]
# F = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498, 415, 941, 803, 850, 311, 992, 489, 367, 598, 914, 930, 224, 517]

huffman(S, F)