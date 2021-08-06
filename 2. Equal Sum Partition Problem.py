def subsetSumDP(l, n, sm):
    dp = [[False for i in range(sm + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if l[i - 1] > sm:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - l[i - 1]]
    
    return dp[-1][-1]


l = [int(x) for x in input().split()]
# o/p: can we divide the array into 2 subsets of equal sum?

total = sum(l)
if total % 2:
    print(False)
else:
    print(subsetSumDP(l, len(l), total // 2))
