from scipy.signal import convolve2d 
import numpy as np

with open('day4/input.txt') as f:
    grid = f.read().replace(",","\n").replace(".","0").replace("@", "1").splitlines()

for i, line in enumerate(grid) :
    grid[i] = list(line)

grid = np.array(grid).astype(int)
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

result = np.array([[1]])
sum = 0
while result.any() != 0:
    padded_grid = np.pad(grid, 1, constant_values=0)
    convolution = convolve2d(padded_grid, kernel, mode="full")
    result = ((convolution[2:-2, 2:-2] < 4) & (grid == 1)).astype(int)
    grid -= result
    sum += result.sum()
    # print(result.sum())
# print(grid)
# print(convolution[2:-2, 2:-2])
# print(result)
print(sum)


                
