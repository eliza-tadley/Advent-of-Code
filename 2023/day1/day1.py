digits_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


# Part 1
def p1(data):
    total = 0
    for d in data:
        nums = ''
        for char in d:
            if char.isnumeric():
                nums += char
        total += int(nums[0] + nums[-1])
    return total


# Part 2
def p2(data):
    total = 0
    for d in data:
        nums = ''
        for i in range(len(d)):
            char = d[i]
            if char.isnumeric():
                nums += char
            else:
                remaining_string = d[i:]
                for key, value in digits_dict.items():
                    if remaining_string.startswith(key):
                        nums += value
        total += int(nums[0] + nums[-1])
    return total


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
