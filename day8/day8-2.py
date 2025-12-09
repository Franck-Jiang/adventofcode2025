import numpy as np
with open('day8/input.txt') as f:
    coords = f.read().splitlines()

circuits = np.array([0 for _ in coords])
boxes = np.array([tuple(map(int, coord.split(","))) for coord in coords])
matrix = np.array([[0 for _ in range(len(boxes))] for _ in range(len(boxes))])

distances = []
for i, box_i in enumerate(boxes):
    for j, box_j in enumerate(boxes):
        matrix[i][j] = sum([(box_i[idx]-box_j[idx])**2 for idx in range(3)])

#can use upper triangle
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        distances.append((matrix[i][j], i, j))
distances = sorted(distances, key=lambda x: x[0], reverse=True)

def is_end(circuit_list):
    if circuit_list[0] == 0:
        return False
    for x in circuit_list[1:]:
        if x != circuit_list[0]:
            return False
    return True

box_i, box_j = 0, 0

while not is_end(circuits):
    dist, box_i, box_j = distances.pop()
    if 0 in [circuits[box_i], circuits[box_j]]:
        if circuits[box_i] == circuits[box_j]:
            circuit_idx = max(circuits) + 1
        else:
            circuit_idx = max(circuits[box_i], circuits[box_j])
    else:
        circuit_idx = min(circuits[box_i], circuits[box_j])
        circuits[circuits == max(circuits[box_i], circuits[box_j])] = circuit_idx
        continue
    circuits[box_i] = circuit_idx
    circuits[box_j] = circuit_idx
res = boxes[box_i][0] * boxes[box_j][0]
print(res)
