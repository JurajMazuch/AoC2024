import os


def is_monotonic_and_within_range(levels):
    differences = [abs(x - y) for x, y in zip(levels, levels[1:])]
    in_range = all(1 <= diff <= 3 for diff in differences)
    is_increasing = all(x < y for x, y in zip(levels, levels[1:]))
    is_decreasing = all(x > y for x, y in zip(levels, levels[1:]))
    return (is_increasing or is_decreasing) and in_range


def part1(data):
    reports = [list(map(int, row.split())) for row in data]
    return sum(1 for levels in reports if is_monotonic_and_within_range(levels))


def part2(data):
    reports = [list(map(int, row.split())) for row in data]
    safe_sum = 0

    #first we try if the whole row meets the condition
    for levels in reports:
        if is_monotonic_and_within_range(levels):
            safe_sum += 1
            continue

        # then we start removing one item at the time and checking if it makes levels safe
        for i in range(len(levels)):
            if is_monotonic_and_within_range(levels[:i] + levels[i + 1:]):
                    safe_sum += 1
                    break

    return safe_sum


with open(os.path.join(os.path.dirname(__file__), 'D02.txt'), 'r') as file:
    input_data = file.readlines()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
