from collections import namedtuple
from random import randint

if __name__ == '__main__':
    count = int(input())

    time = []
    duration = namedtuple("Duration", 'time is_arrival')
    sol, max_sol = 0, 0

    while count:
        arrival, leaving = tuple(map(int, input().split()))
        time.append(duration(arrival, 1))
        time.append(duration(leaving, 0))
        count -= 1

    time.sort(key=lambda x: x.time)

    for item in time:
        if item.is_arrival:
            sol += 1
            max_sol = max(sol, max_sol)
        else:
            sol -= 1

    print(max_sol)
