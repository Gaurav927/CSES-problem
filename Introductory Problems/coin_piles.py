
if __name__=='__main__':
    t = int(input())

    while t:
        a, b = map(int, input().split())

        if (a+b)%3:
            print("NO")
        else:
            if ((2*a - b)>=0 and (2*a - b)%3==0):
                m = (2*a-b)//3
                if m>=0 and a-2*m>=0:

                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        t-=1