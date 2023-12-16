from itertools import product
from tqdm import tqdm


def get_next_value(coordinates, direction, num_columns, num_rows, data):
    if direction == 'R':
        if coordinates[1] + 1 >= num_columns:
            return None, None
        else:
            return data[coordinates[0]][coordinates[1] + 1], (coordinates[0], coordinates[1] + 1)
    elif direction == 'D':
        if coordinates[0] + 1 >= num_rows:
            return None, None
        else:
            return data[coordinates[0]+1][coordinates[1]], (coordinates[0]+1, coordinates[1])
    elif direction == 'L':
        if coordinates[1] - 1 < 0:
            return None, None
        else:
            return data[coordinates[0]][coordinates[1]-1], (coordinates[0], coordinates[1]-1)
    elif direction == 'U':
        if coordinates[0] - 1 < 0:
            return None, None
        else:
            return data[coordinates[0]-1][coordinates[1]], (coordinates[0]-1, coordinates[1])


def get_next_move(coordinates, direct, num_columns, num_rows, data):
    next_moves = []
    next_value, next_coordinates = get_next_value(coordinates, direct, num_columns, num_rows, data)
    if next_value is None:
        return None
    if next_value == '.':
        next_moves.append((next_coordinates, direct))
    elif next_value == '/':
        if direct == 'U':
            next_moves.append((next_coordinates, 'R'))
        elif direct == 'R':
            next_moves.append((next_coordinates, 'U'))
        elif direct == 'D':
            next_moves.append((next_coordinates, 'L'))
        elif direct == 'L':
            next_moves.append((next_coordinates, 'D'))
    elif next_value == "\\":
        if direct == 'U':
            next_moves.append((next_coordinates, 'L'))
        elif direct == 'R':
            next_moves.append((next_coordinates, 'D'))
        elif direct == 'D':
            next_moves.append((next_coordinates, 'R'))
        elif direct == 'L':
            next_moves.append((next_coordinates, 'U'))
    elif next_value == '|':
        if direct in ('U', 'D'):
            next_moves.append((next_coordinates, direct))
        else:
            next_moves.append((next_coordinates, 'U'))
            next_moves.append((next_coordinates, 'D'))
    elif next_value == '-':
        if direct in ('R', 'L'):
            next_moves.append((next_coordinates, direct))
        else:
            next_moves.append((next_coordinates, 'L'))
            next_moves.append((next_coordinates, 'R'))
    return next_moves


# Part 1
def p1(data, starting_position):
    spaces_visited = []
    current_moves = [starting_position]
    num_columns = len(data[0])
    num_rows = len(data)
    while len(current_moves) > 0:
        n = []
        for move in current_moves:
            next_moves = get_next_move(move[0], move[1], num_columns, num_rows, data)
            if next_moves is None:
                continue
            for m in next_moves:
                if m not in spaces_visited:
                    spaces_visited.append(m)
                    n.append(m)
        current_moves = [x for x in n]
    unique_spaces = []
    for s in spaces_visited:
        if s[0] not in unique_spaces:
            unique_spaces.append(s[0])
    return len(unique_spaces)


# Part 2
def p2(data):
    max_unique_spaces = 0
    # try entering from all top row options
    for c in tqdm(range(len(data[0]))):
        unique_spaces = p1(data, ((-1, c), 'D'))
        max_unique_spaces = max(max_unique_spaces, unique_spaces)
    # entering from all left side options
    for r in tqdm(range(len(data))):
        unique_spaces = p1(data, ((r, -1), 'R'))
        max_unique_spaces = max(max_unique_spaces, unique_spaces)
    # entering from all bottoms row options
    for c in tqdm(range(len(data[0]))):
        unique_spaces = p1(data, ((len(data), c), 'U'))
        max_unique_spaces = max(max_unique_spaces, unique_spaces)
    # entering from all right side options
    for r in tqdm(range(len(data))):
        unique_spaces = p1(data, ((r, len(data[0])), 'L'))
        max_unique_spaces = max(max_unique_spaces, unique_spaces)
    return max_unique_spaces


def main():
    with open('./input.txt', 'r') as f:
        data = [list(x.strip()) for x in f.readlines()]

    print("Part 1 Answer: {}".format(p1(data, ((0, -1), 'R'))))
    print("Part 2 Answer: {}".format(p2(data)))


if __name__ == "__main__":
    main()
