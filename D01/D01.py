import os

def part1(data):
    rows = [list(map(int, row.split())) for row in data]

    col1 = sorted([row[0] for row in rows])
    col2 = sorted([row[1] for row in rows])

    return sum([abs(location_id_1 - location_id_2) for location_id_1, location_id_2 in zip(col1, col2)])

def part2(data):
    rows = [list(map(int, row.split())) for row in data]

    col1 = [row[0] for row in rows]
    col2 = [row[1] for row in rows]

    return sum([location_id * col2.count(location_id) for location_id in col1])

with open(os.path.join(os.path.dirname(__file__), 'D01.txt'), 'r') as file:
    input_data = file.readlines()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
