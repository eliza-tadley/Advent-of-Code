from collections import defaultdict


# Part 1
def p1(data):
    part_sums = 0
    for row_num in range(len(data)):
        row = data[row_num]
        # find the numbers in the row (and their starting and ending indexes) and then determine if there is a symbol adjacent to any of the indices
        i = 0
        while i < len(row):
            value = row[i]
            if value.isnumeric():
                for j in range(i+1, len(row)):
                    if row[j].isnumeric():
                        value += row[j]
                    else:
                        break
                # determine if there is a symbol adjacent anywhere to this number
                is_valid = False
                for r in range(row_num - 1, row_num + 2):
                    for c in range(i-1, j+1):
                        if 0 <= r < len(data) and 0 <= c < len(data[0]) and not data[r][c].isnumeric() and data[r][c] != '.':
                            is_valid = True
                if is_valid:
                    part_sums += int(value)
                i = j + 1
            else:
                i += 1
    return part_sums


# Part 2
def p2(data):
    sum_gear_ratios = 0
    possible_gears = {}
    for row_num in range(len(data)):
        row = data[row_num]
        i = 0
        while i < len(row):
            value = row[i]
            if value.isnumeric():
                for j in range(i + 1, len(row)):
                    if row[j].isnumeric():
                        value += row[j]
                    else:
                        break
                # determine if there is a symbol adjacent anywhere to this number
                for r in range(row_num - 1, row_num + 2):
                    for c in range(i - 1, j + 1):
                        if 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] == '*':
                            if (r, c) in possible_gears:
                                possible_gears[(r, c)].append(int(value))
                            else:
                                possible_gears[(r,c)] = [int(value)]
                i = j + 1
            else:
                i += 1
    for loc, nums in possible_gears.items():
        if len(nums) == 2:
            sum_gear_ratios += (nums[0] * nums[1])
    return sum_gear_ratios


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
