def maxVal(n, w, val, wt):
    dp = [0 for i in range(w + 1)]

    for i in range(w + 1):
        for j in range(n):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[-1]


n, w = [int(x) for x in input().split()]
val = [int(x) for x in input().split()]
wt = [int(x) for x in input().split()]

print(maxVal(n, w, val, wt))
