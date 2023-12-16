from tqdm import tqdm
from copy import deepcopy


def calc_slide_north(grid):
    while True:
        num_moves = 0
        for r in range(1, len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 'O':
                    if grid[r-1][c] == '.':
                        grid[r][c] = '.'
                        grid[r-1][c] = 'O'
                        num_moves += 1
        if num_moves == 0:
            return grid


def calc_slide_south(grid):
    while True:
        num_moves = 0
        for r in range(len(grid)-1):
            for c in range(len(grid[r])):
                if grid[r][c] == 'O':
                    if grid[r+1][c] == '.':
                        grid[r][c] = '.'
                        grid[r+1][c] = 'O'
                        num_moves += 1
        if num_moves == 0:
            return grid


def calc_slide_east(grid):
    while True:
        num_moves = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])-1):
                if grid[r][c] == 'O':
                    if grid[r][c+1] == '.':
                        grid[r][c] = '.'
                        grid[r][c+1] = 'O'
                        num_moves += 1
        if num_moves == 0:
            return grid


def calc_slide_west(grid):
    while True:
        num_moves = 0
        for r in range(len(grid)):
            for c in range(1, len(grid[r])):
                if grid[r][c] == 'O':
                    if grid[r][c-1] == '.':
                        grid[r][c] = '.'
                        grid[r][c-1] = 'O'
                        num_moves += 1
        if num_moves == 0:
            return grid


# Part 1
def p1(data):
    new = calc_slide_north(data)
    total_load = 0
    for r in range(len(new)):
        num_round = 0
        for c in range(len(data[r])):
            if data[r][c] == 'O':
                num_round += 1
        total_load += ((len(new) - r) * num_round)
    return total_load


# Part 2
def p2(data, num_rotations):
    for i in tqdm(range(num_rotations)):
        data = calc_slide_north(data)
        data = calc_slide_west(data)
        data = calc_slide_south(data)
        data = calc_slide_east(data)
        # if i == 1000:
        #     grid_100 = deepcopy(data)
        # if i > 1000 and data == grid_100:
        #     print(i)
    total_load = 0
    for r in range(len(data)):
        num_round = 0
        for c in range(len(data[r])):
            if data[r][c] == 'O':
                num_round += 1
        total_load += ((len(data) - r) * num_round)
    return total_load


def main():
    with open('./input.txt', 'r') as f:
        data = [list(x.strip()) for x in f.readlines()]

    # test: 999999996 mod 7 = 2

    # real: after starting at 1000 it seems to cycle in 42
    # 1000000000 - 1000 = 999999000
    # 999999000 mod 42 = 0
    # so just do 1000

    print("Part 1 Answer: {}".format(p1(data)))
    print("Part 2 Answer: {}".format(p2(data, 1000)))


if __name__ == "__main__":
    main()
