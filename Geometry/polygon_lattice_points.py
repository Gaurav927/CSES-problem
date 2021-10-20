import math
def area(point1, point2):
    return point1[0]*point2[1] - point1[1]* point2[0]

def boundary_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    return math.gcd(abs(x1-x2), abs(y1-y2)) - 1


if __name__=='__main__':
    sides = int(input())
    coordinates = []
    while sides:
        coordinates.append(tuple(map(int, input().split())))
        sides-=1
        
    total_area = area(coordinates[-1], coordinates[0])
    bounday_count = boundary_points(coordinates[-1], coordinates[0])
    for i in range(len(coordinates)-1):
        total_area += area(coordinates[i], coordinates[i+1])
        bounday_count+=  boundary_points(coordinates[i], coordinates[i+1])
        
    total_area = abs(total_area)//2
    bounday_count += len(coordinates)
    internal_count = total_area + 1 - (bounday_count)//2
    print(internal_count, bounday_count)
