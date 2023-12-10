def parse_data(data):
    cleaned_data = []
    for d in data:
        cleaned_data.append([int(x) for x in d.split(' ')])
    return cleaned_data


# Part 1
def p1(data):
    sum_values = 0
    for history in data:
        current = history
        last_values = []
        while not all(x == 0 for x in current):
            new = [j-i for i, j in zip(current[:-1], current[1:])]
            last_values.append(current[-1])
            current = new
        to_add = 0
        for v in reversed(last_values):
            new_value = v + to_add
            to_add = new_value
        sum_values += to_add
    return sum_values


# Part 2
def p2(data):
    sum_values = 0
    for history in data:
        current = history
        first_values = []
        while not all(x == 0 for x in current):
            new = [j - i for i, j in zip(current[:-1], current[1:])]
            first_values.append(current[0])
            current = new
        to_add = 0
        for v in reversed(first_values):
            new_value = v - to_add
            to_add = new_value
        sum_values += to_add
    return sum_values


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    data = parse_data(data)

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
