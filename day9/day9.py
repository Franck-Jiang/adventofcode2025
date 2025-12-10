import numpy as np

with open('day9/input0.txt') as f:
    coords = f.read().splitlines()

tiles = np.array([list(map(int, coord.split(","))) for coord in coords])
max_diff = 0
for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        diff = abs(tiles[i] - tiles[j] + 1)
        if max_diff < diff[0] * diff[1]:
            max_diff = diff[0] * diff[1]

print(max_diff)