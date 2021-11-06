if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    maps = []

    for _ in range(n):
        maps.append(list(input()))

    def isValid(row, col, maps, visited):
        if row < 0 or row >= n or col < 0 or col >= m or visited[row][col] or maps[row][col] == '#':
            return False
        return True

    def dfs(visited, maps, row, col):

        visited[row][col] = True
        if isValid(row + 1, col, maps, visited):
            dfs(visited, maps, row + 1, col)
        if isValid(row - 1, col, maps, visited):
            dfs(visited, maps, row - 1, col)
        if isValid(row, col + 1, maps, visited):
            dfs(visited, maps, row, col + 1)
        if isValid(row, col - 1, maps, visited):
            dfs(visited, maps, row, col - 1)
        return

    def bfs(visited, maps, row, col):
        queue = []
        queue.append((row, col))

        while len(queue) > 0:

            row, col = queue.pop()
            visited[row][col] = True
            if isValid(row + 1, col, maps, visited):
                queue.append((row + 1, col))
            if isValid(row - 1, col, maps, visited):
                queue.append((row - 1, col))
            if isValid(row, col + 1, maps, visited):
                queue.append((row, col + 1))
            if isValid(row, col - 1, maps, visited):
                queue.append((row, col - 1))

    count = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] == '.':
                bfs(visited, maps, i, j)
                count += 1

    print(count)


