import numpy as np

with open('day1/input.txt') as f:
    lines = np.array(f.read().replace("L", "-").replace("R", "").splitlines()).astype(int)

dial = 50
password = 0
for line in lines:
    dial = (dial + line)%100
    if dial == 0:
        password += 1
print(password)
