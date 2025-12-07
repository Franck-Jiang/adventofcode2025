with open('day7/input.txt') as f:
    room = f.read().splitlines()

x_len = len(room)
y_len = len(room[0])
beam = [room[0].index("S")]
split_time = 0

for line in room:
    print(line)

for x in range(1, x_len):
    new_beam = list()
    new_room = room[x]
    while len(beam) > 0:
        b = beam.pop()
        if room[x][b] == ".":
            new_room = new_room[:b] + "|" + new_room[b+1:]
            new_beam.append(b)
        elif room[x][b] == "^":
            new_room = new_room[:b-1] + "|X|" + new_room[b+2:]
            new_beam.append(b-1)
            new_beam.append(b+1)
            split_time += 1
    beam = set(new_beam)
    room[x] = new_room
    print(room[x])

print(split_time)
