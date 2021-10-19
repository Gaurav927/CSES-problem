from functools import lru_cache
mod = 10**9 + 7
if __name__== '__main__':
    n = int(input())
    n = 100
    @lru_cache(maxsize=None)
    def helper(n):
        if n<0:
            return 0
        if n==0:
            return 1
        sol = 0
        for i in range(1, 7):
            sol += helper(n-i)
        return sol%mod
    
    print(helper(n)%mod)
    
