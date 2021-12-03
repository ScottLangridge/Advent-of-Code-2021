import numpy as np


def main(raw_input):
    report = np.array([list(line) for line in raw_input.splitlines()])

    o2_report = report.copy()
    co2_report = report.copy()

    while len(o2_report) > 1:
        # For each column index
        for i in range(len(report[0, :])):
            most_common_bit = most_common(o2_report[:, i])
            o2_report = np.array(list(filter(lambda line: line[i] == most_common_bit, o2_report)))
            if len(o2_report) == 1:
                break

    while len(co2_report) > 1:
        # For each column index
        for i in range(len(report[0, :])):
            least_common_bit = least_common(co2_report[:, i])
            co2_report = np.array(list(filter(lambda line: line[i] == least_common_bit, co2_report)))
            if len(co2_report) == 1:
                break

    return int(''.join(o2_report[0]), 2) * int(''.join(co2_report[0]), 2)


def most_common(lst):
    lst = list(lst)
    ones = lst.count('1')
    zeros = lst.count('0')
    if zeros > ones:
        return '0'
    else:
        return '1'


def least_common(lst):
    lst = list(lst)
    ones = lst.count('1')
    zeros = lst.count('0')
    if ones < zeros:
        return '1'
    else:
        return '0'


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
