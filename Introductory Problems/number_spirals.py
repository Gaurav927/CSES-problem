def getNum(row, col):

    if row>col:
        if row%2==0:
            return row**2 - col + 1
        return (row-1)**2 + col
    else:
        if col%2==1:
            return col**2 - row + 1

        return (col-1)**2 + row

if __name__=='__main__':
    t = int(input())
    # print(getNum(1000000000, 1000000000))
    while t:
        row, col = map(int, input().split())
        print(getNum(row, col))
        t-=1
        

