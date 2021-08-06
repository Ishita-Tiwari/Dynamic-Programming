import math
def dpSolution(l, n):
    '''
    This problem statement is a variation of equal sum partition!
    sum of part 1 = s1
    sum of part 2 = total - s1
    we need to minimise their difference ie, (total - s1) - s1
    that is, we need to minimize total - 2s1

    The solution is similar to subset sum problem. Basically, we know
    that the sum of elements can range from min to sum(l). We will find
    all the possible valid sums.
    The last row of dp[][] has True if it can be obtained else False.
    Now that we have all the valid values of s1, substitute in the above
    formula and find the lowest value

    '''
    
    total = sum(l)
    dp = [[False for j in range(total + 1)] for i in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if l[i - 1] > total:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - l[i - 1]]
    ans = math.inf
    for i in range(total + 1):
        if dp[-1][i]:
            ans = min(ans, abs(total - 2 * i))

    return ans
    
    


def mySolution(l, n):
    '''
    Consider: 2, 4, 5, 10, 11
    this will consider {11} then {11, 2} then {11, 2, 4} so on
    it will give minimum diff = 2

    the correct answer is 0 if we divide it as:
    {11, 5} and {10, 2, 4}

    Hence, this is WRONG. DO NOT use this.
    '''
    l.sort()
    total = sum(l)
    p1, p2 = max(l), total - max(l)
    ans = abs(p1 - p2)
    lb, ub = 0, n - 1
    total = p2

    for i in range(n - 1):
        p1 += l[i]
        p2 -= l[i]
        ans = min(ans, abs(p1 - p2))
    return ans


l = [int(x) for x in input().split()]
print(dpSolution(l, len(l)))
