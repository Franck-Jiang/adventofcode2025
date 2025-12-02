import numpy as np

with open('day2/input.txt') as f:
    lines = f.read().replace(",","\n").splitlines()

invalid_ids = 0

for id_range in lines:
    start, end = id_range.split("-")
    for i in range(int(start), int(end)+1):
        half_id_len = int(len(str(i))/2)
        if half_id_len*2 == len(str(i)):
            if str(i)[:half_id_len] == str(i)[half_id_len:]:
                invalid_ids += i
        else:
            pass

print(invalid_ids)