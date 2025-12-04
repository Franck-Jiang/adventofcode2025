

with open('day3/input.txt') as f:
    lines = f.read().replace(",","\n").splitlines()

sum = 0
for line in lines:
    l_line = list(line)
    max_val = ""
    for digit_i in range(12, 0, -1):
        max_digit = max(l_line[-digit_i::-1])
        max_idx = l_line.index(max_digit)
        max_val += max_digit

        l_line = l_line[max_idx+1:]

    print(max_val)
    max_val = int(max_val)
    sum += max_val

print(sum)
