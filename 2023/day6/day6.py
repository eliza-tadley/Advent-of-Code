def parse_data(data):
    times = [int(x) for x in data[0].split(':')[1].split(' ') if x != '']
    distances = [int(x) for x in data[1].split(':')[1].split(' ') if x != '']
    return times, distances


def parse_data_part2(data):
    time = int(''.join([x for x in data[0].split(':')[1].split(' ') if x != '']))
    distance = int(''.join([x for x in data[1].split(':')[1].split(' ') if x != '']))
    return time, distance


def calculate_num_wins(time, distance_record):
    nums_wins = 0
    for i in range(time):
        dist = i * (time - i)
        if dist > distance_record:
            nums_wins += 1
    return nums_wins


# Part 1
def p1(times, distances):
    product_wins = 1
    for i in range(len(times)):
        num_wins = calculate_num_wins(times[i], distances[i])
        product_wins *= num_wins
    return product_wins


# Part 2
def p2(time, distance):
    return calculate_num_wins(time, distance)


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    times, distances = parse_data(data)
    time, distance = parse_data_part2(data)

    print("Part 1 Answer: {}".format(p1(times, distances)))
    print("Part 2 Answer: {}".format(p2(time, distance)))


if __name__ == "__main__":
    main()
