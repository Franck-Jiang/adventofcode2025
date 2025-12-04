from scipy.signal import convolve2d 
import numpy as np

with open('day4/input.txt') as f:
    grid = f.read().replace(",","\n").replace(".","0").replace("@", "1").splitlines()

#padding
for i, line in enumerate(grid) :
    grid[i] = list("0"+line+"0")

grid.insert(0, ["0" for _ in range(len(grid[0]))])
grid.append(["0" for _ in range(len(grid[0]))])

grid = np.array(grid).astype(int)
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

convolution = convolve2d(grid, kernel, mode="full")
result = (convolution[2:-2, 2:-2] < 4) & (grid[1:-1, 1:-1] == 1)
# print(grid[1:-1, 1:-1])
# print(convolution[2:-2, 2:-2])
print(result.sum())


                
