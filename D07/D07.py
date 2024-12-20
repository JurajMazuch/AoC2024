import os
from itertools import product


def is_correct(numbers, operators, expected_result):
    result = numbers[0]

    for i, num in enumerate(numbers[1:]):
        if operators[i] == '+':
            result += num
        elif operators[i] == '*':
            result *= num
        elif operators[i] == '|':
            result = int(str(result) + str(num))

    return result == expected_result

def sum_correct_rows(data, operators):
    correct_rows_sum = 0

    for row in data:
        expected_result = int(row.split(':')[0])
        numbers = list(map(int, row.split(':')[1].strip().split(' ')))
        operator_combinations = product(operators, repeat=len(numbers) - 1)

        if any(is_correct(numbers, ops, expected_result) for ops in operator_combinations):
            correct_rows_sum += expected_result

    return correct_rows_sum

with open(os.path.join(os.path.dirname(__file__), 'D07_Test.txt'), 'r') as file:
    input_data = [line.strip() for line in file]

print("Part 1:", sum_correct_rows(input_data, '+*'))
print("Part 2:", sum_correct_rows(input_data, '+*|'))
