with open('day6/input.txt') as f:
    problems = f.read().splitlines()

line = len(problems)
width = len(problems[0])

for a in problems:
    if len(a) != width:
        raise ValueError("not aligned")

operation = list()
sum = 0
for y in range(width-1, -1, -1):
    number = ""
    for x in range(line - 1):
        if problems[x][y] != " ":
            number += problems[x][y]
    if number != "":
        operation.append(number)
    
    if problems[-1][y] != " ":
        sum += eval(problems[-1][y].join(operation))
        operation = list()
print(sum)