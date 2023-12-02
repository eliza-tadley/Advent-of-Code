from collections import defaultdict


def parse_data(data):
    clean_data = {}
    for game in data:
        id_and_subsets = game.split(':')
        game_id = int(id_and_subsets[0].split(' ')[-1])
        subsets = id_and_subsets[1].split(';')
        clean_data[game_id] = subsets
    return clean_data


# Part 1
def p1(data, available_cubes):
    sum_ids = 0
    for game_id, subsets in data.items():
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        is_possible = True
        for s in subsets:
            if not is_possible:
                break
            cube_counts = s.strip().split(',')
            for c in cube_counts:
                if not is_possible:
                    break
                c_color = c.strip().split(' ')[1].strip()
                c_count = int(c.strip().split(' ')[0].strip())
                if c_count > available_cubes[c_color]:
                    is_possible = False
                    break
        if is_possible:
            sum_ids += game_id
    return sum_ids


# Part 2
def p2(data):
    sum_powers = 0
    for subsets in data.values():
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        min_nums = defaultdict(int)
        for s in subsets:
            cube_counts = s.strip().split(',')
            for c in cube_counts:
                c_color = c.strip().split(' ')[1].strip()
                c_count = int(c.strip().split(' ')[0].strip())
                if c_count > min_nums[c_color]:
                    min_nums[c_color] = c_count
        power = 1
        for value in min_nums.values():
            power *= value
        sum_powers += power
    return sum_powers


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]
    clean_data = parse_data(data)

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    available_cubes = {'red': 12, 'green': 13, 'blue': 14}
    print("Part 1 Answer: {}".format(p1(clean_data, available_cubes)))
    print("Part 2 Answer: {}".format(p2(clean_data)))


if __name__ == "__main__":
    main()
