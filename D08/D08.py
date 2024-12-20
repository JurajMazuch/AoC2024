import os
import re


def subtract_points(p1, p2):
    return (a - b for a, b in zip(p1, p2))

def scale_vector(v, scalar):
    return tuple(scalar * x for x in v)

def get_antinode(p1, p2, scale=2):
    v = subtract_points(p2, p1)  # create a vector out of points
    v = scale_vector(v, scale)  # scale as necessary
    antinode = (p1[0] + v[0], p1[1] + v[1])  # move the vector to starting point
    return antinode

def is_in_map(point, point_map):
    return 0 <= point[0] < len(point_map[0]) and 0 <= point[1] < len(point_map)

def collect_antennas(data):
    antennas = {}
    for y in range(len(data)):
        for m in re.finditer("[a-zA-Z0-9]", data[y]):
            x = m.start()
            frequency = data[y][x]
            if frequency not in antennas:
                antennas[frequency] = []
            antennas[frequency].append((x, y))
    return antennas

def part1(data):
    antennas = collect_antennas(data)
    antinodes = set()
    for coordinates in antennas.values():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                for p1, p2 in [(coordinates[i], coordinates[j]), (coordinates[j], coordinates[i])]:
                    antinode = get_antinode(p1, p2)
                    if is_in_map(antinode, data):
                        antinodes.add(antinode)
    return len(antinodes)

def part2(data):
    antennas = collect_antennas(data)
    antinodes = set()
    for coordinates in antennas.values():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                for p1, p2 in [(coordinates[i], coordinates[j]), (coordinates[j], coordinates[i])]:
                    scale = 1
                    while True:
                        antinode = get_antinode(p1, p2, scale)
                        if is_in_map(antinode, data):
                            antinodes.add(antinode)
                        else:
                            break
                        scale += 1
    return len(antinodes)

with open(os.path.join(os.path.dirname(__file__), 'D08.txt'), 'r') as file:
    input_data = [line.strip() for line in file]

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
