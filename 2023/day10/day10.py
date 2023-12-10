import matplotlib.path as mpltPath


def parse_data(data):
    cleaned_data = []
    for d in data:
        cleaned_data.append(list(d))
    return cleaned_data


# Part 1
def p1(data, starting_point, starting_dir):
    total_steps = 0
    current_point = starting_point
    current_dir = starting_dir
    while True:
        if current_dir == 'S':
            next_point = (current_point[0]+1, current_point[1])
        elif current_dir == 'N':
            next_point = (current_point[0]-1, current_point[1])
        elif current_dir == 'W':
            next_point = (current_point[0], current_point[1]-1)
        else:
            next_point = (current_point[0], current_point[1]+1)
        next_value = data[next_point[0]][next_point[1]]
        total_steps += 1
        if next_value == 'S':
            break
        elif next_value == '|' and current_dir == 'S':
            next_dir = 'S'
        elif next_value == '|' and current_dir == 'N':
            next_dir = 'N'
        elif next_value == '-' and current_dir == 'E':
            next_dir = 'E'
        elif next_value == '-' and current_dir == 'W':
            next_dir = 'W'
        elif next_value == 'L' and current_dir == 'S':
            next_dir = 'E'
        elif next_value == 'L' and current_dir == 'W':
            next_dir = 'N'
        elif next_value == 'J' and current_dir == 'S':
            next_dir = 'W'
        elif next_value == 'J' and current_dir == 'E':
            next_dir = 'N'
        elif next_value == '7' and current_dir == 'N':
            next_dir = 'W'
        elif next_value == '7' and current_dir == 'E':
            next_dir = 'S'
        elif next_value == 'F' and current_dir == 'N':
            next_dir = 'E'
        elif next_value == 'F' and current_dir == 'W':
            next_dir = 'S'
        current_point = next_point
        current_dir = next_dir
    return int(total_steps/2)


# Part 2
def p2(data, starting_point, starting_dir):
    all_points = []
    current_point = starting_point
    current_dir = starting_dir
    while True:
        if current_dir == 'S':
            next_point = (current_point[0] + 1, current_point[1])
        elif current_dir == 'N':
            next_point = (current_point[0] - 1, current_point[1])
        elif current_dir == 'W':
            next_point = (current_point[0], current_point[1] - 1)
        else:
            next_point = (current_point[0], current_point[1] + 1)
        next_value = data[next_point[0]][next_point[1]]
        all_points.append(next_point)
        if next_value == 'S':
            break
        elif next_value == '|' and current_dir == 'S':
            next_dir = 'S'
        elif next_value == '|' and current_dir == 'N':
            next_dir = 'N'
        elif next_value == '-' and current_dir == 'E':
            next_dir = 'E'
        elif next_value == '-' and current_dir == 'W':
            next_dir = 'W'
        elif next_value == 'L' and current_dir == 'S':
            next_dir = 'E'
        elif next_value == 'L' and current_dir == 'W':
            next_dir = 'N'
        elif next_value == 'J' and current_dir == 'S':
            next_dir = 'W'
        elif next_value == 'J' and current_dir == 'E':
            next_dir = 'N'
        elif next_value == '7' and current_dir == 'N':
            next_dir = 'W'
        elif next_value == '7' and current_dir == 'E':
            next_dir = 'S'
        elif next_value == 'F' and current_dir == 'N':
            next_dir = 'E'
        elif next_value == 'F' and current_dir == 'W':
            next_dir = 'S'
        current_point = next_point
        current_dir = next_dir
    path = mpltPath.Path(all_points)
    num_points_inside = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if path.contains_point((r, c)) and (r,c) not in all_points:
                num_points_inside += 1
    return num_points_inside


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    data = parse_data(data)

    starting_point = (63, 62)      # test input = (2,0), main input = (63, 62), big test = (0, 4)
    starting_dir = 'S'          # test input = S, main input = S or N

    print("Part 1 Answer: {}".format(p1(data, starting_point, starting_dir)))
    print("Part 2 Answer: {}".format(p2(data, starting_point, starting_dir)))


if __name__ == "__main__":
    main()
