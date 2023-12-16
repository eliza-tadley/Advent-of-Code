from itertools import product
from tqdm import tqdm


def parse_data(data):
    results = []
    for d in data:
        x = d.split(' ')
        nums = [int(i) for i in x[1].split(',')]
        results.append((list(x[0]), nums))
    return results


def get_data_part2(data):
    new_data = []
    for d in data:
        springs = d[0]
        nums = d[1]
        new_springs = []
        new_springs.extend(springs)
        new_springs.append('?')
        new_springs.extend(springs)
        new_springs.append('?')
        new_springs.extend(springs)
        new_springs.append('?')
        new_springs.extend(springs)
        new_springs.append('?')
        new_springs.extend(springs)
        new_nums = []
        new_nums.extend(nums)
        new_nums.append(',')
        new_nums.extend(nums)
        new_nums.append(',')
        new_nums.extend(nums)
        new_nums.append(',')
        new_nums.extend(nums)
        new_nums.append(',')
        new_nums.extend(nums)
        new_data.append((new_springs, new_nums))
    return new_data


def do_records_match(springs, nums):
    previous_spring = False
    groups = []
    current_group = ''
    for s in springs:
        if s == '.':
            if previous_spring:
                groups.append(current_group)
                current_group = ''
            previous_spring = False
        elif s == '#':
            current_group += '#'
            previous_spring = True
    if previous_spring:
        groups.append(current_group)
    #print(f'groups: {groups}')
    #print(f"nums: {nums}")
    if len(nums) != len(groups):
        return False
    for i in range(len(nums)):
        if nums[i] != len(groups[i]):
            return False
    return True


# Part 1
def p1(data):
    total_arrangements = 0
    li = ['.', '#']
    for j in tqdm(range(len(data))):
        s = data[j]
        #print(f"line: {s}")
        num_questions = s[0].count('?')
        combs = [''.join(comb) for comb in product(li, repeat=num_questions)]
        for comb in combs:
            comb_index = 0
            new_arrangement = []
            for c in s[0]:
                if c == '?':
                    new_arrangement.append(comb[comb_index])
                    comb_index += 1
                else:
                    new_arrangement.append(c)
            #print(f"new arrangement: {new_arrangement}")
            if do_records_match(new_arrangement, s[1]):
                total_arrangements += 1
        #print(f"total arrangements: {total_arrangements}")
    return total_arrangements


# Part 2
def p2(data):
    pass


def main():
    with open('./input_test.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    data = parse_data(data)
    data_part2 = get_data_part2(data)

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p1(data_part2)))


if __name__ == "__main__":
    main()
