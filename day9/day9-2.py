import numpy as np
from shapely.geometry import Polygon, box

with open('day9/input.txt') as f:
    coords = f.read().splitlines()

tiles = np.array([list(map(int, coord.split(","))) for coord in coords])
polygon = Polygon(tiles)
max_diff = 0
max_sub = []

# for i in range(len(tiles)):
#     for j in range(i, len(tiles)):
#         x1, y1 = tiles[i]
#         x2, y2 = tiles[j]
#         sub_polygon = box(x1, y1, x2, y2)
#         if polygon.contains(sub_polygon):      
#             diff = abs(tiles[i] - tiles[j] + 1)
#             # print(sub_polygon, tiles[i], tiles[j])  
#             if max_diff < diff[0] * diff[1]:
#                 max_diff = diff[0] * diff[1]
#                 max_sub = sub_polygon
# # 1474444748


# https://github.com/mgtezak/Advent_of_Code/blob/master/2025/09/p2.py
def part2():
    corners = [tuple(map(int, coord.split(','))) for coord in coords]
    n = len(corners)

    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((corners[i], corners[i-1])))
        for j in range(i+1, n):
            c1, c2 = sorted((corners[i], corners[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size


print(part2())

