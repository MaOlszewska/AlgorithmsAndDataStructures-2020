''' Mamy r kul czerwonych, b kul niebieskich i g ul zielonych. Zadaniem jest znalezienie całkowitą liczbe
ustawien w których kule tego samego koloru nie stoją obok siebie.'''

'''Jeśli ostania była kulą czerwoną to mamy DP(r, b, g, red) = DP(r, b - 1, g, blue) + DP(r, b, g - 1, green)
Jeśli ostatnią braną kulą była niebieska to DP(r, b, g, blue) = DP(r - 1, b, g, red) + DP(r, b, g - 1, green)
OStania brana to zielona DP(r, b, g, green) = DP(r - 1, b, g, red) + DP(r, b - 1, g, blue)'''


def DP(r, b, g, prev):
    if r < 0 or g < 0 or b < 0:
        return 0
    if r == 0 and b == 0 and g == 0:
        return 1
    if prev == 'r':
        return DP(r, b - 1, g, 'b') + DP(r, b, g - 1, 'g')
    if prev == 'b':
        return DP(r - 1, b, g, 'r') + DP(r, b, g - 1, 'g')
    if prev == 'g':
        return DP(r - 1, b, g, 'r') + DP(r, b - 1, g, 'b')


def count(r, b, g):
    return DP(r - 1,b, g, 'r') + DP(r, b - 1, g, 'b') + DP(r, b, g - 1, 'g')
