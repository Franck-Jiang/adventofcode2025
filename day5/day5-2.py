with open('day5/input.txt') as f:
    database = f.read().replace(",","\n").replace(".","0").replace("@", "1").split("\n\n")

str_range_id = database[0].splitlines()
available_ingredients = list(map(int, database[1].splitlines()))
ranges = sorted([list(map(int, start_end_range.split("-"))) for start_end_range in str_range_id], key=lambda x: x[0])

min_id, max_id = ranges[0]
fresh_ingredients = max_id - min_id + 1

for range_ids in ranges[1:]:
    if range_ids[0] <= max_id:
        if range_ids[1] > max_id:
            fresh_ingredients += range_ids[1] - max_id
            max_id = range_ids[1]
        continue
    else:
        min_id, max_id = range_ids
        fresh_ingredients += max_id - min_id + 1

print(fresh_ingredients)
