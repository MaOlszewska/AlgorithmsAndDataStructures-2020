''' Mająć nieposortowaną tablice liczb całkowitych, które reprezentują klucze drzewa skonstruuj
zrównoważone drzewo BST '''

'Po posortowaniu kluczy rosnący nasz korzeń bedzie śrdokowym elementem, lewe poddrzewo tworzymy z ' \
'elementów, które znajudą się w tablicy po lewej stronie korzenia, a prawe poddrzewo z prawej strony ' \
'korzenia.'
class BSTNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.right = None
        self.left = None

def BalancedTree( keys, minimum, maximum, root):
    if minimum > maximum:
        return root
    mid = (maximum + minimum) // 2
    root = BSTNode(keys[mid], None)
    root.left = BalancedTree(keys, minimum, mid - 1, root.left)
    root.right = BalancedTree(keys,mid + 1, maximum,root.right)
    return root

def print_inorder(root, tree):  # rosnąco
    if root is not None:
        print_inorder(root.left, tree)
        tree.append(root.key)
        print_inorder(root.right, tree)
    return tree

def construct(keys):
    keys.sort()
    return BalancedTree(keys, 0, len(keys) - 1, None)

if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]
    print(print_inorder(construct(keys),  []))
