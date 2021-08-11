def longestPalindromicSubsequence(s1, s2, n):
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
    
    
# print the length of longest palindromic subsequence
s1 = input()
s2 = s1[::-1]
print(longestPalindromicSubsequence(s1, s2, len(s1)))
