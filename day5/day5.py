with open('day5/input.txt') as f:
    database = f.read().replace(",","\n").replace(".","0").replace("@", "1").split("\n\n")

str_range_id = database[0].splitlines()
available_ingredients = list(map(int, database[1].splitlines()))

fresh_ingredients = 0
ranges = sorted([list(map(int, start_end_range.split("-"))) for start_end_range in str_range_id], key=lambda x: x[0])

for ingredient in available_ingredients:
    for range_ids in ranges:
        if ingredient >= range_ids[0] and ingredient <= range_ids[1]:
            fresh_ingredients += 1
            break
        elif ingredient < range_ids[0]:
            break

print(fresh_ingredients)
