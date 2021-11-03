if __name__ == '__main__':
    n, total = list(map(int, input().split()))
    array = list(map(int, input().split()))
    updated = False

    for i in range(n):
        target = total - array[i]
        store = {}
        for j in range(i):
            if target - array[j] in store:
                updated = True
                print(store[target - array[j]] + 1, j + 1, i + 1)
            store[array[j]] = j

            if updated:
                break
        if updated:
            break

    if not updated:
        print("IMPOSSIBLE")
