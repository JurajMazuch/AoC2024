def parse_input(file_path):
    with open(file_path, "r") as file:
        first_part, second_part = file.read().split("\n\n")
        constraints = [tuple(map(int, line.split("|"))) for line in first_part.split("\n")]
        rows = [list(map(int, row.split(","))) for row in second_part.split("\n")]
        return constraints, rows

def is_valid_row(row, constraints):
    for x, y in constraints:
        if x in row and y in row:
            if row.index(x) > row.index(y):  # X must come before Y
                return False
    return True

def order_row(row, constraints):
    modified = True
    while modified:
        modified = False
        for x, y in constraints:
            if x in row and y in row:
                xi, yi = row.index(x), row.index(y)
                if xi > yi:  # X comes after Y, so reorder
                    row.pop(xi)
                    row.insert(yi, x)
                    modified = True
    return row

def middle_item(row):
    mid = len(row) // 2
    return row[mid - 1] if len(row) % 2 == 0 else row[mid]

def process_rows(file_path):
    constraints, rows = parse_input(file_path)
    valid_rows = []
    ordered_rows = []

    for row in rows:
        if is_valid_row(row, constraints):
            valid_rows.append(row)
        else:
            ordered_rows.append(order_row(row, constraints))

    # Calculate sums
    sum_valid = sum(middle_item(row) for row in valid_rows)
    sum_invalid = sum(middle_item(row) for row in ordered_rows)

    return sum_valid, sum_invalid


# Solve the puzzle
sum_valid, sum_invalid = process_rows("D05.txt")
print(f"Sum of middle items from valid rows: {sum_valid}")
print(f"Sum of middle items from ordered invalid rows: {sum_invalid}")