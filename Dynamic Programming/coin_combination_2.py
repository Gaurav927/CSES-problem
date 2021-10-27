
from functools import lru_cache
if __name__=='__main__':

    with open('test_input_1.txt', 'r') as file:
        data = file.readlines()

    num_coin, amount = map(int, data[0].split())
    # num_coin, amount = 3, 2000
    # print(amount)

    coins = list(map(int, data[1].split()))
    print(coins)
    # coins = [1000, 1500, 1]

    mod = 10**9 + 7

    dp = [[0]*(amount+1) for _ in range(num_coin+1)]

    for i in range(num_coin):
        dp[i+1][0] = 1
    
    for i in range(amount):
        dp[0][i] = 0

    for i in range(1, num_coin+1):
        for pay in range(min(coins), amount+1):
            dp[i][pay] = dp[i-1][pay]% mod
            dp[i][pay] += dp[i][pay-coins[i-1]] if pay-coins[i-1]>=0 else 0
            dp[i][pay] = dp[i][pay]%mod
    
    print(dp[num_coin][amount])

    @lru_cache(maxsize=None)
    def helper(i, target):

        if target==amount:
            return 1
        
        if target>amount or i>=num_coin:
            return 0

        return helper(i, target+ coins[i]) + helper(i+1, target)

    
    # print(helper(0, 0))