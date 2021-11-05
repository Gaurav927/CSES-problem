from functools import lru_cache
if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))

    @lru_cache(maxsize=None)
    def helper(i, j):
        if i == j:
            return array[i]

        return max(array[i] - helper(i+1, j), array[j] - helper(i, j-1))

    # print((sum(array) + helper(0, n-1))//2)

    dp = [[0]*n for _ in range(n)]

    for start in range(n-1, -1, -1):
        for end in range(start, n, 1):
            if start == end:
                dp[start][end] = array[start]
            else:
                dp[start][end] = max(array[start] - dp[start + 1][end], array[end] - dp[start][end - 1])

    print((sum(array) + dp[0][n-1])//2)




