if __name__=='__main__':
    t = int(input())
    while t:
        x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        
        if area ==0:
            print("TOUCH")
        elif area<0:
            print("RIGHT")
        else:
            print('LEFT')
        
        t-=1
