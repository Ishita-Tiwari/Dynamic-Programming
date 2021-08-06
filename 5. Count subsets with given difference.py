def subsetGivenDiff(l, n, diff):
    '''
    s2 - s1 = diff
    total - s1 - s1 = diff
    total - 2s1 = diff
    total - diff = 2s1
    (total - diff) // 2 = s1

    if you rearrange it, you can also get (total + diff) // 2

    now, we know what the value of s1 must be. so, we can find the number of
    subsets whose sum is (total - diff) // 2
    '''
    
    sm = (sum(l) + diff) // 2
    
    dp = [[0 for j in range(sm + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if l[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - l[i - 1]]


    ans = dp[-1][-1]
    return ans



l = [int(x) for x in input().split()]
diff = int(input())
print(subsetGivenDiff(l, len(l), diff))
