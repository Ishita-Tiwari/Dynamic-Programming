from sys import maxsize

# it is of the size (n + 1) * (n + 1)
dp = [[-1 for j in range(1001)] for i in range(1001)]
def mcmMemoized(arr, i, j):
    if i >= j:
        dp[i][j] = 0
        return dp[i][j]
    if dp[i][j] != -1:
        return dp[i][j]

    mn = maxsize
    for k in range(i, j):
        temp = mcmMemoized(arr, i, k) + mcmMemoized(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        mn = min(temp, mn)
    dp[i][j] = mn
    return mn


def mcmRecursive(arr, i, j):
    if i >= j:
        return 0
    mn = maxsize

    '''
    we perform recursive calls on both the parts
    the extra part arr[i - 1] * arr[k] * arr[j] represents
    the multiplication of those two parts
    '''
    
    for k in range(i, j):
        temp = mcmRecursive(arr, i, k) + mcmRecursive(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        mn = min(temp, mn)
    return mn
        
    

arr = [int(x) for x in input().split()]
print(mcmRecursive(arr, 1, len(arr) - 1))
print(mcmMemoized(arr, 1, len(arr) - 1))
