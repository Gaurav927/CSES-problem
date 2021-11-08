if __name__ == '__main__':
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    median = sticks[n // 2]
    print(sum([abs(length - median) for length in sticks]))
