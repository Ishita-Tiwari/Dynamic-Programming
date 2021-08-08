from sys import maxsize

def onedDP(coin, n, sm):
    dp = [(sm + 1) for i in range(sm + 1)]
    dp[0] = 0
    for i in range(sm + 1):
        for j in range(n):
            if coin[j] <= i:
                dp[i] = min(dp[i], dp[i - coin[j]] + 1)
    if dp[-1] != sm + 1:
        return dp[-1]
    else:
        return -1

def coinChangeMinCoins(coin, n, sm):

    # initialization
    dp = [[0 for j in range(sm + 1)] for i in range(n + 1)]
    for i in range(sm + 1):
        dp[0][i] = maxsize - 1
    for i in range(1, sm + 1):
        if i % coin[0] == 0:
            dp[1][i] = i // coin[0]
        else:
            dp[1][i] = maxsize - 1


    # logic
    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if coin[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coin[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    if dp[-1][-1] == maxsize - 1 or dp[-1][-1] == maxsize:
        return -1
    return dp[-1][-1]
    


coin = [int(x) for x in input().split()]
sm = int(input())
print(coinChangeMinCoins(coin, len(coin), sm))
print(onedDP(coin, len(coin), sm))
