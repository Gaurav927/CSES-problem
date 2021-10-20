def area(point1, point2):
    return point1[0]*point2[1] - point1[1]* point2[0]

if __name__=='__main__':
    sides = int(input())
    coordinates = []
    while sides:
        coordinates.append(tuple(map(int, input().split())))
        sides-=1
        
    total_area = area(coordinates[-1], coordinates[0])
    for i in range(len(coordinates)-1):
        total_area += area(coordinates[i], coordinates[i+1])

    print(abs(total_area))
    

