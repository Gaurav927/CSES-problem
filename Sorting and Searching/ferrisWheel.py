from bisect import bisect_left
if __name__ == '__main__':
    n, max_weight = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    weights.sort()
    sol = 0
    start, end = 0, n - 1

    while end >= start:
        if weights[start] + weights[end] > max_weight:
            end -= 1
        else:
            start += 1
            end -= 1

        sol += 1
    print(sol)






