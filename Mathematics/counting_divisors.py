import math

import bisect
def search(primes, n):
    return bisect.bisect_right(primes, n)
    
if __name__=='__main__':

    t = int(input())

    numbers = []

    while t:
        numbers.append(int(input()))
        t-=1
    n = max(numbers)
    primes = [True for _ in range(n+1)]
    
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            step = i
            i = i + i
            while i<= n:
                primes[i] = False
                i+=step
    dup_primes = primes[:]
    primes = [i for i in range(len(primes)) if primes[i]]

    for n in numbers:
        if dup_primes[n]:
            print(2)
        else:
            factors = {}
            index = search(primes, int(math.sqrt(n)+1))

            for fact in primes[:index+1]:
                while n>0 and n%fact==0:
                    factors[fact] = factors.get(fact, 0) + 1
                    n=n//fact
            if dup_primes[n]:
                factors[n] = 1
            count = 1
            for key in factors:
                count *= (factors[key]+1)
            print(count)


    

            
            
    
                
                