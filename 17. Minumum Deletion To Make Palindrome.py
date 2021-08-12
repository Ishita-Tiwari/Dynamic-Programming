def minDelPal(s1, s2, n):
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return (n - dp[-1][-1])


# minimum number of deletions to make a string palindromic
s1 = input()
s2 = s1[::-1]
print(minDelPal(s1, s2, len(s1)))
