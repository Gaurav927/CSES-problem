
if __name__ == '__main__':
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    store, updated, sol = {}, False, (None, None)

    for i in range(n):
        if target - array[i] in store:
            sol = (store[target - array[i]], i+1)
            updated = True
            break
        store[array[i]] = i + 1
    if updated:
        print(sol[0], sol[1])
    else:
        print("IMPOSSIBLE")

