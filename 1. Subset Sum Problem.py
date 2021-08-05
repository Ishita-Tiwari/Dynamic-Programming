'''DP solution'''
def subSumDp(dp, l, sm, n):
    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if l[i - 1] > sm:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - l[i - 1]]
    return dp[-1][-1]
    

'''Recursive solution!'''
def subsetSum(l, sm, n):
    if sm == 0:
        return True
    if n == 0:
        return False
    if(l[n - 1] > sm):
        return (subsetSum(l, sm, n - 1))
    return( subsetSum(l, sm, n - 1) or subsetSum(l, sm - l[n - 1], n - 1))


sm = int(input())
l = [int(x) for x in input().split()]
n = len(l)


##initialization
dp = [[False for j in range(sm + 1)] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(sm + 1):
        if j == 0:
            dp[i][j] = True
##for i in dp:
##    print(*i)


print('recursion:    ', subsetSum(l, sm, n))
print('Dynamic Prog: ', subSumDp(dp, l, sm, n))
print()
