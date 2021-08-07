def coinChange(coin, n, sm):

    # initialization
    dp = [0 for i in range(sm + 1)]
    dp[0] = 1

    # logic
    for i in range(n):
        for j in range(sm + 1):
            if coin[i] <= j:
                dp[j] += dp[j - coin[i]]
    
    return dp[-1]
    

def twodDP(coin, n, sm):
    dp = [[0 for j in range(sm + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if coin[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]
    

coin = [int(x) for x in input().split()]
sm = int(input())
print(coinChange(coin, len(coin), sm))
print(twodDP(coin, len(coin), sm))
