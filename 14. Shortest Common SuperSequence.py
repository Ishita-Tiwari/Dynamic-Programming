def shortestCommonSupersequence(s1, s2, n1, n2):
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]

    '''
    Length of shortest common supersequence:
    max possible length - length of max common subsequence
    '''
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return (n1 + n2 - dp[-1][-1])
    


s1 = input()
s2 = input()
n1, n2 = len(s1), len(s2)
print(shortestCommonSupersequence(s1, s2, n1, n2))
