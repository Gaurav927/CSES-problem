mod = 1e9 + 7

def helper(n):
    sol = 0
    
    while n>0:
        sol += n//5
        n =n//5
    return sol
if __name__=='__main__':
    n = int(input())
    
    print(helper(n))