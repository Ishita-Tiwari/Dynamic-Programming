def rodCutting(price, n):
    dp = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if j < i:
                dp[i] = max(dp[i], dp[i - j - 1] + price[j])
    return dp[-1]


#ln = [int(x) for x in input().split()] # this may or may not be given
price = [int(x) for x in input().split()]
n = int(input()) #total length of the rod

print(rodCutting(price, n))
