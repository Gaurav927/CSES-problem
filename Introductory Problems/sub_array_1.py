if __name__ == '__main__':

    n, total = map(int, input().split())
    array = map(int, input().split())
    store = {0: 1}
    prefixSum, sol = 0, 0

    for item in array:
        prefixSum += item
        store[prefixSum] = store.get(prefixSum, 0) + 1
        sol += store.get(prefixSum - total, 0)
    print(sol)
