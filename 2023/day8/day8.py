from math import lcm


def parse_data(data):
    directions = list(data[0])
    locations = {}
    for i in range(2,len(data)):
        # AAA = (BBB, BBB)
        x = data[i].split(' = ')
        locations[x[0]] = (x[1][1:4], x[1][6:9])
    return directions, locations


# Part 1
def p1(directions, locations):
    not_at_end = True
    num_steps = 0
    direction_index = 0
    current_location = 'AAA'
    while not_at_end:
        current_direction = directions[direction_index]
        if current_direction == 'L':
            next_location = locations[current_location][0]
        else:
            next_location = locations[current_location][1]
        num_steps += 1
        if next_location == 'ZZZ':
            not_at_end = False
        else:
            current_location = next_location
            if direction_index + 1 >= len(directions):
                direction_index = 0
            else:
                direction_index += 1
    return num_steps


def get_starting_nodes(locations):
    starting_nodes = []
    for node in locations:
        if node.endswith('A'):
            starting_nodes.append(node)
    return starting_nodes


# Part 2
def p2(directions, locations, current_nodes):
    num_first_steps = []
    next_starting_nodes = []
    for node in current_nodes:
        not_at_end = True
        num_steps = 0
        direction_index = 0
        current_location = node
        while not_at_end:
            current_direction = directions[direction_index]
            if current_direction == 'L':
                next_location = locations[current_location][0]
            else:
                next_location = locations[current_location][1]
            num_steps += 1
            if next_location.endswith('Z'):
                not_at_end = False
            current_location = next_location
            if direction_index + 1 >= len(directions):
                direction_index = 0
            else:
                direction_index += 1
        num_first_steps.append(num_steps)
        next_starting_nodes.append(current_location)
    #print(f"steps to cycle: {num_first_steps}")
    ans = lcm(num_first_steps[0], num_first_steps[1])
    for i in range(2, len(num_first_steps)):
        ans = lcm(ans, num_first_steps[i])
    return ans


def test_steps(directions, locations, starting_node):
    steps_to_end = []
    i = 0
    current_location = starting_node
    direction_index = 0
    while i < 10:
        not_at_end = True
        num_steps = 0
        while not_at_end:
            current_direction = directions[direction_index]
            if current_direction == 'L':
                next_location = locations[current_location][0]
            else:
                next_location = locations[current_location][1]
            num_steps += 1
            if next_location.endswith('Z'):
                not_at_end = False
            current_location = next_location
            if direction_index + 1 >= len(directions):
                direction_index = 0
            else:
                direction_index += 1
        steps_to_end.append(num_steps)
        i += 1
    print(f"Number of steps to end: {steps_to_end}")


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    directions, locations = parse_data(data)
    starting_nodes = get_starting_nodes(locations)          # ['VNA', 'AAA', 'DPA', 'JPA', 'DBA', 'QJA']

    #test_steps(directions, locations, starting_node)
    # from this test I learned that the starting nodes to ending nodes always repeat in a cycle of the same number of steps

    print("Part 1 Answer: {}".format(p1(directions, locations)))
    print("Part 2 Answer: {}".format(p2(directions, locations, starting_nodes)))


if __name__ == "__main__":
    main()
