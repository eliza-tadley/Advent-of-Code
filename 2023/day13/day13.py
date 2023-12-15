def parse_data(data):
    patterns = []
    p = []
    for i in data:
        if i != '\n':
            p.append(list(i.strip()))
        else:
            patterns.append(p.copy())
            p = []
    patterns.append(p.copy())
    return patterns


def calculate_counts(pattern):
    # check if any vertical reflection
    num_cols = len(pattern[0])
    for c in range(1, num_cols):
        if check_if_vertical_reflection(c, pattern):
            return c, 0
    # check if any horizontal reflection
    num_rows = len(pattern)
    for r in range(1, num_rows):
        if check_if_horizontal_reflection(r, pattern):
            return 0, r
    return 0, 0


def check_if_vertical_reflection(col_num, data):
    # find the minimum columns to an edge either left or right
    min_cols = min(len(data[0]) - col_num, col_num)
    # check if the columns match up from either side starting from the min distance away
    for c in range(col_num - min_cols, col_num):
        for r in range(len(data)):
            if data[r][c] != data[r][col_num + (col_num - c) - 1]:
                return False
    return True


def check_if_horizontal_reflection(row_num, data):
    # find the minimum rows to an edge either above or below
    min_rows = min(len(data) - row_num, row_num)
    # check if the rows match up from either side starting from the min distance away
    for c in range(len(data[0])):
        for r in range(row_num - min_rows, row_num):
            if data[r][c] != data[row_num + (row_num - r) - 1][c]:
                return False
    return True


def calculate_counts_part2(pattern):
    # check if any vertical reflection
    num_cols = len(pattern[0])
    for c in range(1, num_cols):
        if calc_vertical_reflection_differences(c, pattern) == 1:
            return c, 0
    # check if any horizontal reflection
    num_rows = len(pattern)
    for r in range(1, num_rows):
        if calc_horizontal_reflection_differences(r, pattern) == 1:
            return 0, r
    return 0, 0


def calc_vertical_reflection_differences(col_num, data):
    num_diff = 0
    # find the minimum columns to an edge either left or right
    min_cols = min(len(data[0]) - col_num, col_num)
    # check if the columns match up from either side starting from the min distance away
    for c in range(col_num - min_cols, col_num):
        for r in range(len(data)):
            if data[r][c] != data[r][col_num + (col_num - c) - 1]:
                num_diff += 1
    return num_diff


def calc_horizontal_reflection_differences(row_num, data):
    num_diff = 0
    # find the minimum rows to an edge either above or below
    min_rows = min(len(data) - row_num, row_num)
    # check if the rows match up from either side starting from the min distance away
    for c in range(len(data[0])):
        for r in range(row_num - min_rows, row_num):
            if data[r][c] != data[row_num + (row_num - r) - 1][c]:
                num_diff += 1
    return num_diff


# Part 1
def p1(data):
    sum_columns_left = 0
    sum_rows_above = 0
    for pattern in data:
        nums_col_left, num_row_above = calculate_counts(pattern)
        sum_columns_left += nums_col_left
        sum_rows_above += num_row_above
    return sum_columns_left + (100 * sum_rows_above)


# Part 2
def p2(data):
    sum_columns_left = 0
    sum_rows_above = 0
    for pattern in data:
        nums_col_left, num_row_above = calculate_counts_part2(pattern)
        sum_columns_left += nums_col_left
        sum_rows_above += num_row_above
    return sum_columns_left + (100 * sum_rows_above)


def main():
    with open('./input.txt', 'r') as f:
        data = f.readlines()

    data = parse_data(data)

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
