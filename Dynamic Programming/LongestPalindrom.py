def longestPalindrome(string, i, j, DP):
    if i == j:
        return 1
    if i > j:
        return 0
    if string[i] == string[j]:
        if DP[i][j] is None:
            DP[i][j] = 2 + longestPalindrome(string, i + 1, j - 1, DP)
    else:
        if DP[i][j] is None:
            DP[i][j] = max(longestPalindrome(string, i + 1, j, DP), longestPalindrome(string, i, j - 1, DP))
    return DP[i][j]

def Palindrome(string):
    n = len(string)
    DP = [[None for _ in range(n)] for _ in range(n)]
    return longestPalindrome(string, 0, n - 1, DP)


