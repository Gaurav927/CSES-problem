from functools import lru_cache
if __name__=='__main__':

    length, bredth = map(int, input().split())

    if length==bredth:
        print(0)
    elif length==1 or bredth==1:
        print(length-1 if bredth==1 else bredth-1)
    
   
    else:

        dp = [[length*bredth]*(bredth+1) for _ in range(length+1)]

        for i in range(1, length+1):
            for j in range(1, bredth+1):

                if i==j or i==1 or j==1:
                    if i==j:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = i-1 if j==1 else j-1
                else:

                    for cut in range(1, i):
                        dp[i][j] = min(dp[i][j], 1 + dp[cut][j] + dp[i-cut][j])
                    
                    for cut in range(1, j):
                        dp[i][j] = min(dp[i][j], 1 + dp[i][cut] + dp[i][j-cut])

        print(dp[length][bredth])

    @lru_cache(maxsize=None)
    def helper(l, b):

        if l==b:
            return 0
        sol = float('inf')
        for i in range(1, l):
           
            sol = min(sol, 1 + helper(i, b) + helper(l-i, b))

        for i in range(1, b):
            sol = min(sol, 1+ helper(l, i) + helper(l, b-i))

        return sol

    # print(helper(length, bredth))