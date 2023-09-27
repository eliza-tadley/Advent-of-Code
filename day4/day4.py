# Part 1
from collections import defaultdict
import operator


def p1(total_sleep_times, count_min_asleep):
    # find the guard that has the most min asleep
    guard_id = max(total_sleep_times.items(), key=operator.itemgetter(1))[0]
    # find minute that this guard spends asleep the most
    min_most_asleep = max(count_min_asleep[guard_id].items(), key=operator.itemgetter(1))[0]
    return guard_id * min_most_asleep


def p2(count_min_asleep):
    min_most_asleep_by_guard = {}
    for guard in count_min_asleep:
        min_most_asleep, count_min_most_asleep = max(count_min_asleep[guard].items(), key=operator.itemgetter(1))
        min_most_asleep_by_guard[guard] = (min_most_asleep, count_min_most_asleep)
    max_min_most_sleep = 0
    guard_max_min_most_sleep = 0
    min_min_most_sleep = 0
    for g in min_most_asleep_by_guard:
        if min_most_asleep_by_guard[g][1] > max_min_most_sleep:
             max_min_most_sleep = min_most_asleep_by_guard[g][1]
             guard_max_min_most_sleep = g
             min_min_most_sleep = min_most_asleep_by_guard[g][0]
    return guard_max_min_most_sleep * min_min_most_sleep


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    data.sort()
    total_sleep_times = defaultdict(int)
    count_min_asleep = defaultdict(lambda: defaultdict(int))
    for d in data:
        current_min = int(d.split(' ')[1].split(':')[1].replace(']', ''))
        if '#' in d:
            current_guard_id = int(d.split(' ')[3].replace('#', ''))
        elif 'falls' in d:
            asleep_min = current_min
        elif 'wakes' in d:
            awake_min = current_min
            for i in range(asleep_min, awake_min):
                total_sleep_times[current_guard_id] += 1
                count_min_asleep[current_guard_id][i] += 1

    print("Part 1 Answer: {}".format(p1(total_sleep_times, count_min_asleep)))
    print("Part 2 Answer: {}".format(p2(count_min_asleep)))


if __name__ == "__main__":
    main()