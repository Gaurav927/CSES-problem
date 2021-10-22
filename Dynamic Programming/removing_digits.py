
if __name__ =='__main__':
    n = int(input())
    
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for char in str(i):
            dp[i] = min(dp[i- int(char)]+1, dp[i])
    
    print(dp[i])