from collections import namedtuple
if __name__ == '__main__':
    n = int(input())
    movie = namedtuple('movie', 'start end')
    time = []
    while n:
        start, end = tuple(map(int, input().split()))
        time.append(movie(start, end))
        n -= 1
    time.sort(key=lambda x: x.end)
    current, sol = time[0].end, 0

    for m in time:
        if m.start >= current:
            sol += 1
            current = m.end
    print(sol + 1)



