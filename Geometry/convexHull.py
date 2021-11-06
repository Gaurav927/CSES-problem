if __name__ == '__main__':
    n = int(input())
    points = []

    while n:
        points.append(tuple(map(int, input().split())))
        n -= 1
    points = sorted(points, key=lambda p: (p[0], p[1]))


    def cross(o, a, b):

        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    print(len(set(lower[:-1] + upper[:-1])))
    for point in list(set(lower[:-1] + upper[:-1])):
        print(' '.join(str(x) for x in point))
