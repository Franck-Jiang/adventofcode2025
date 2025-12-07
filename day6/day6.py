with open('day6/input.txt') as f:
    problems = f.read().splitlines()

def remove_void(list_with_void: list) -> list:
    while True:
        try:
            list_with_void.remove("")
        except ValueError:
            return list_with_void

t_numbers = list()
for problem in problems[:-1]:
    t_str_numbers = problem.split(" ")
    t_str_numbers = remove_void(t_str_numbers)
    t_numbers.append(t_str_numbers)

numbers = [[t_numbers[y][x] for y in range(len(t_numbers))] for x in range(len(t_numbers[0]))]

operations = problems[-1].split(" ")
operations = remove_void(operations)

sum = 0
for i in range(len(operations)):
    operation = operations[i].join(numbers[i]) 
    sum += eval(operation)
print(sum)