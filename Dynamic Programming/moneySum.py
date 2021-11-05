if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    total = sum(coins)
    money = [[False] * (total + 1) for _ in range(n + 1)]
    solution = set()

    for i in range(n+1):
        money[i][0] = True
    for amount in range(min(coins), total + 1):
        for i in range(1, n + 1):
            money[i][amount] = money[i - 1][amount]
            if amount - coins[i - 1] >= 0:
                money[i][amount] = money[i][amount] or money[i-1][amount - coins[i - 1]]
            if money[i][amount]:
                solution.add(amount)

    print(len(solution))
    print(' '.join(str(ele) for ele in sorted(list(solution))))
