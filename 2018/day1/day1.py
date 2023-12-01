
# Part 1
def p1(data):
    current_frequency = 0
    for change in data:
        current_frequency += int(change)
    return current_frequency


# Part 2
def p2(data):
    found_frequencies = set()
    current_frequency = 0
    while True:
        for change in data:
            current_frequency += int(change)
            if current_frequency in found_frequencies:
                return current_frequency
            found_frequencies.add(current_frequency)


def main():
    with open('./input.txt', 'r') as f:
        data = f.readlines()

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
