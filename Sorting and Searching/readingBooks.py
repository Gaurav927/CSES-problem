if __name__ == '__main__':
    n = int(input())
    books = list(map(int, input().split()))
    print(max(sum(books), max(books)*2))