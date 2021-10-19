mod = 10**9 + 7

def power(x, y):
	res = 1
	while (y > 0):
		if ((y & 1) == 1) :
			res = (res * x)%mod
		y = y >> 1
		x = (x * x)%mod
	
	return res%mod


if __name__=='__main__':
    
    t = int(input())
    while t:
        a, b = list(map(int, input().split()))
        if a==0 and b!=0:
            print(0)
        elif b==0:
            print(1)
        elif b==1:
            print(a%mod)
        else:
            print(power(a,b))    
        t-=1
    
        
        
    
