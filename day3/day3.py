with open('day3/input.txt') as f:
    lines = f.read().replace(",","\n").splitlines()

sum = 0
for line in lines:
    l_line = list(line)

    max_digit = max(l_line[:-1])
    max_idx = l_line.index(max_digit)
    trunc_line = l_line[max_idx+1:]
    max2_digit = max(trunc_line)
    max2_idx = trunc_line.index(max2_digit)
    max_val = int(max_digit+max2_digit)
    sum += max_val

print(sum)
