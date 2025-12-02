import numpy as np
import time


with open('day2/input.txt') as f:
    lines = f.read().replace(",","\n").splitlines()

time_start = time.time_ns()

invalid_ids = 0
for id_range in lines:
    start, end = id_range.split("-")
    for id in range(int(start), int(end)+1):
        id_len = len(str(id))        
        for n in range(2, id_len + 1):
            subdiv_len = int(id_len/n)
            if subdiv_len == id_len/n:
                invalid = True
                for i_n in range(1, n):
                    invalid = (str(id)[subdiv_len*(i_n-1):subdiv_len*(i_n)] == str(id)[subdiv_len*(i_n):subdiv_len*(i_n+1)]) & invalid
                    if not invalid:
                        break
                else: #hehe
                    invalid_ids += id
                    break

print(f"TIME: {time.time_ns() - time_start}")
print(invalid_ids)