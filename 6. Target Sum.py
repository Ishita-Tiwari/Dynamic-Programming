from math import ceil
def targetSumDP(l, target):
    n = len(l)
    sm = ceil((target + sum(l)) / 2)

    dp = [[0 for j in range(sm + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if l[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - l[i - 1]]
    print(sm)
    for i in dp:
        print(*i)
    return dp[-1][-1]

    

l = [int(x) for x in input().split()]
sm = int(input())

print(targetSumDP(l, sm))
