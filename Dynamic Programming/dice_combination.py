
if __name__=='__main__':
    n = int(input())
    mod = 10**9 + 7
    
    dp = [0]*(n+2)
    dp[1] = 1
    
    for i in range(1, n+2):
        for j in range(1, 7):
            if i >=j:
                dp[i] = (dp[i] + dp[i-j]) %mod
    
    print(dp[-1])