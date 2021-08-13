def longestRepeatingSubsequence(s, n):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
    

# print the length of longest repeating subsequence
s = input()
n = len(s)
print(longestRepeatingSubsequence(s, n))
