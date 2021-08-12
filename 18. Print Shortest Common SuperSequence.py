def printSCS(s1, s2, n1, n2):
    dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    ind1, ind2 = n1, n2
    ans = ""
    while(ind1 > 0 and ind2 > 0):
        if s1[ind1 - 1] == s2[ind2 - 1]:
            ans = s1[ind1 - 1] + ans
            ind1 -= 1
            ind2 -= 1
        else:
            if dp[ind1 - 1][ind2] >= dp[ind1][ind2 - 1]:
                ans = s1[ind1 - 1] + ans
                ind1 -= 1
                
            else:
                ans = s2[ind2 - 1] + ans
                ind2 -= 1
    while(ind1 > 0):
        ans = s1[ind1 - 1] + ans
        ind1 -= 1
    while(ind2 > 0):
        ans = s2[ind2 - 1] + ans
        ind2 -= 1
    return ans


# print the shortest common supersequence
s1 = input()
s2 = input()
n1, n2 = len(s1), len(s2)
print(printSCS(s1, s2, n1, n2))
