def lcsTopDown(s1, s2, n1, n2):
    dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

    

dpMemo = [[-1 for i in range(1005)] for j in range(1005)]
def lcsMemo(s1, s2, ind1, ind2):
    if ind1 == 0 or ind2 == 0:
        dpMemo[ind1][ind2] = 0
        return dpMemo[ind1][ind2]
    if dpMemo[ind1][ind2] != -1:
        return dpMemo[ind1][ind2]
    if s1[ind1 - 1] == s2[ind2 - 1]:
        dpMemo[ind1][ind2] = 1 + lcsRecursive(s1, s2, ind1 - 1, ind2 - 1)
        return dpMemo[ind1][ind2]
    dpMemo[ind1][ind2] = max(lcsRecursive(s1, s2, ind1, ind2 - 1), lcsRecursive(s1, s2, ind1 - 1, ind2))
    return dpMemo[ind1][ind2]
    



def lcsRecursive(s1, s2, ind1, ind2):
    if ind1 == 0 or ind2 == 0:
        return 0
    if s1[ind1 - 1] == s2[ind2 - 1]:
        return(1 + lcsRecursive(s1, s2, ind1 - 1, ind2 - 1))

    return(max(lcsRecursive(s1, s2, ind1, ind2 - 1),
               lcsRecursive(s1, s2, ind1 - 1, ind2)))
    


# print the length of longest common subsequence
s1 = input()
s2 = input()
print(lcsRecursive(s1, s2, len(s1), len(s2)))
print(lcsMemo(s1, s2, len(s1), len(s2)))
##print(dpMemo[len(s1)][len(s2)])
print(lcsTopDown(s1, s2, len(s1), len(s2)))
