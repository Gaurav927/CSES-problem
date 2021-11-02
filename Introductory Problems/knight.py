if __name__=='__main__':
    t = int(input())

    for n in range(1, t+1):
        print(int((n**2)*(n**2 - 1)/2- 4*(n-1)*(n-2)))