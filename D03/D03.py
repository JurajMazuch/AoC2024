import os
import re
import math


def part1(data):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return sum(int(a) * int(b) for a, b in matches)


def part2(data):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    enabled = True
    result = 0
    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            result += math.prod(map(int, re.findall(r"\d+", m)))
    return result


with open(os.path.join(os.path.dirname(__file__), 'D03.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
