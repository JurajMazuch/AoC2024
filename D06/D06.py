import os


directions = {
    '<': (0, -1),
    '>': (0, 1),
    'V': (1, 0),
    '^': (-1, 0)
}

def find_guard(map):
    for x, row in enumerate(map):
        for y, value in enumerate(row):
            if value in ['<', '^', '>', 'V']:
                return x, y
    return None

def turn_right(current_direction):
    direction_order = ['<', '^', '>', 'V']
    return direction_order[(direction_order.index(current_direction) + 1) % 4]

def is_in_map(x, y, map):
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def follow_path(map):
    x, y = find_guard(map)
    direction = map[x][y]
    dx, dy = directions[direction]
    visited_positions = set()

    while is_in_map(x + dx, y + dy, map):
        if (x, y, direction) in visited_positions:
            raise Exception(f"Infinite loop detected at position ({x}, {y}) with direction {direction}.")
        visited_positions.add((x, y, direction))

        if map[x + dx][y + dy] == '#':
            direction = turn_right(direction)
            dx, dy = directions[direction]
        else:
            x, y = x + dx, y + dy

    return visited_positions

def part1(map):
    try:
        visited_positions = follow_path(map)
    except Exception as e:
        print(e)
        return 0

    return len({(x, y) for x, y, _ in visited_positions}) + 1


def part2(map):
    obstacle_positions = 0
    #brute force
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] != '.':
                continue

            altered_map = [row[:] for row in map]
            row = list(altered_map[x])
            row[y] = '#'
            altered_map[x] = ''.join(row)

            try:
                follow_path(altered_map)
            except Exception as e:
                obstacle_positions += 1

    return  obstacle_positions


with open(os.path.join(os.path.dirname(__file__), 'D06.txt'), 'r') as file:
    input_data = [line.strip() for line in file]

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
