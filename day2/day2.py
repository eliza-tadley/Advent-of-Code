from collections import defaultdict


# Part 1
def p1(data):
    count_two, count_three = 0, 0
    for box in data:
        count_letters = defaultdict(int)
        for l in box:
            count_letters[l] += 1
        if 2 in count_letters.values():
            count_two += 1
        if 3 in count_letters.values():
            count_three += 1
    return count_two * count_three


# Part 2
def compare_boxes(box1, box2):
    # check if two boxes differ by exactly one character
    # if they do then return the characters in common
    letters = zip(box1, box2)
    same = ''.join(a for a, b in letters if a == b)
    if len(same) == len(box1) - 1:
        return same
    return


def p2(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            box1 = data[i]
            box2 = data[j]
            result = compare_boxes(box1, box2)
            if result:
                return ''.join(result)


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
