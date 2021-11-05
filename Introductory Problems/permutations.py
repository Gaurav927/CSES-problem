if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    elif n <= 3:
        print("NO SOLUTION")
    else:
        print(' '.join( [str(even) for even in range(1, n+1) if even % 2 == 0] + [str(odd) for odd in range(1, n+1) if odd % 2]))

