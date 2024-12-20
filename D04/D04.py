import os

def part1(data):
    word = 'XMAS'
    rows = len(data)
    cols = len(data[0])
    word_length = len(word)
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (-1, 0),  # up
        (0, -1),  # left
        (-1, -1),  # diagonal up-left
        (-1, 1),  # diagonal up-right
        (1, -1),  # diagonal down-left
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                end_r = r + (word_length - 1) * dr
                end_c = c + (word_length - 1) * dc
                if 0 <= end_r < rows and 0 <= end_c < cols:
                    x, y = r, c
                    match = True
                    for i in range(word_length):
                        if not is_valid(x, y) or data[x][y] != word[i]:
                            match = False
                            break
                        x += dr
                        y += dc
                    if match:
                        count += 1
    return count


def part2(data):
    rows = len(data)
    cols = len(data[0])
    count = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == 'A':
                NW = data[r - 1][c - 1]
                NE = data[r + 1][c - 1]
                SW = data[r - 1][c + 1]
                SE = data[r + 1][c + 1]
                if (
                        ((NW == 'M' and SE == 'S') or (NW == 'S' and SE == 'M')) and
                        ((NE == 'M' and SW == 'S') or (NE == 'S' and SW == 'M'))
                ):
                    count += 1
    return count

with open(os.path.join(os.path.dirname(__file__), 'D04.txt'), 'r') as file:
    input_data = [line.strip() for line in file]

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
