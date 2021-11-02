mod = 1e9 + 7

def pow(n):
    # if n<=1:
    #     return n+1
    
    # if n%2:
    #     x = pow((n-1)//2)%mod
    #     return (2* x*x)%mod
    # x = pow(n//2)%mod
    # return (x*x)%mod

    ans = 1

    for i in range(n):
        ans*= 2
        ans = ans%mod
    return ans
if __name__=='__main__':
    n = int(input())

    print(int(pow(n)))

