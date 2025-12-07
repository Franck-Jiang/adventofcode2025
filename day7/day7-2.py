with open('day7/input.txt') as f:
    room = f.read().splitlines()

x_len = len(room)
y_len = len(room[0])
timelines = {room[0].index("S"): 1}
timelines_count = 1

for x in range(1, x_len):
    new_beam = {}
    new_room = room[x]
    while len(timelines) > 0:
        b, occurence = timelines.popitem()
        if room[x][b] == ".":
            try:
                new_beam[b] += occurence
            except KeyError:
                new_beam[b] = occurence
        elif room[x][b] == "^":
            timelines_count += occurence
            try:
                new_beam[b-1] += occurence
            except KeyError:
                new_beam[b-1] = occurence

            try:
                new_beam[b+1] += occurence
            except KeyError:
                new_beam[b+1] = occurence
    timelines = new_beam
    room[x] = new_room
    print(room[x])


print(timelines_count)
