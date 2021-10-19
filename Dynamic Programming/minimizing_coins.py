from functools import lru_cache
def main(coins, amount, bank):
    @lru_cache(maxsize=None)
    def helper(index, amount):
        if amount ==0 or amount in bank:
            return 0 if amount==0 else 1
        if index>=len(coins) or amount<0:
            return float('inf')
        
        coin = coins[index]
        sol = float('inf')
        
        for i in range(amount//coin + 1):
            sol = min(sol, i + helper(index+1, amount - i*coin))
        return sol

    return helper(0, amount)



def iterative(coins, amount):
    
    dp = [amount+1]*(amount +1)
    dp[0] = 0
    
    for coin in coins:
        for pay in range(1, amount+1):
            if pay-coin>=0:
                dp[pay] =  min(1+ dp[pay-coin], dp[pay])
    
    return dp[-1]
    

if __name__=='__main__':
    number, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    number_of_coin = iterative(coins, amount)
    
    
    if number_of_coin>amount:
        print(-1)
    else:
        print(number_of_coin)
    


