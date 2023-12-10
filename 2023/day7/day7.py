from collections import Counter


card_strength = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
card_strength_2 = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}


def order_hand(hand):
    ordered = sorted(list(hand), key=lambda x: card_strength[x], reverse=True)
    bids = ''.join(ordered)
    return bids


def get_hand_strength(hand):
    # 7 - five of a kind
    if 5 in Counter(hand).values():
        return 7
    # 6 - four of a kind
    if 4 in Counter(hand).values():
        return 6
    # 5 - full house
    if 3 in Counter(hand).values() and 2 in Counter(hand).values():
        return 5
    # 4 - three of a kind
    if 3 in Counter(hand).values():
        return 4
    # 3 - two pair
    if Counter(list(Counter(hand).values()))[2] == 2:
        return 3
    # 2 - one pair
    if 2 in Counter(hand).values():
        return 2
    # 1 - high card aka everything else
    return 1


def get_hand_strength_part2(hand):
    # 7 - five of a kind
    if 5 in Counter(hand).values() or (4 in Counter(hand).values() and Counter(hand)['J'] == 1) or \
            (3 in Counter(hand).values() and Counter(hand)['J'] == 2) or \
            (2 in Counter(hand).values() and Counter(hand)['J'] == 3) or \
            (1 in Counter(hand).values() and Counter(hand)['J'] == 4):
        return 7
    # 6 - four of a kind
    if 4 in Counter(hand).values() or (3 in Counter(hand).values() and Counter(hand)['J'] == 1) or\
            (Counter(list(Counter(hand).values()))[2] == 2 and Counter(hand)['J'] == 2) or \
            (1 in Counter(hand).values() and Counter(hand)['J'] == 3):
        return 6
    # 5 - full house
    if 3 in Counter(hand).values() and 2 in Counter(hand).values() or (Counter(list(Counter(hand).values()))[2] == 2 and Counter(hand)['J'] == 1) or \
            (3 in Counter(hand).values() and Counter(hand)['J'] == 2) or \
            (Counter(list(Counter(hand).values()))[2] == 2 and Counter(hand)['J'] == 2):
        return 5
    # 4 - three of a kind
    if 3 in Counter(hand).values() or (2 in Counter(hand).values() and Counter(hand)['J'] == 1) or (Counter(hand)['J'] == 2):
        return 4
    # 3 - two pair
    if Counter(list(Counter(hand).values()))[2] == 2 or (Counter(hand)['J'] == 2):
        return 3
    # 2 - one pair
    if 2 in Counter(hand).values() or (Counter(hand)['J'] == 1):
        return 2
    # 1 - high card aka everything else
    return 1


def parse_data(data):
    hands = {}
    bids = {}
    for line in data:
        x = line.split(' ')
        strength = get_hand_strength(x[0])
        hands[x[0]] = strength
        bids[x[0]] = int(x[1])
    return hands, bids


def parse_data_part2(data):
    hands = {}
    bids = {}
    for line in data:
        x = line.split(' ')
        strength = get_hand_strength_part2(x[0])
        hands[x[0]] = strength
        bids[x[0]] = int(x[1])
    return hands, bids


# Part 1
def p1(hands, bids):
    winnings = 0
    ordered_hands = sorted(hands, key=lambda x: (hands[x], card_strength[x[0]], card_strength[x[1]], card_strength[x[2]], card_strength[x[3]], card_strength[x[4]]))
    for i in range(len(ordered_hands)):
        rank = i + 1
        bid = bids[ordered_hands[i]]
        winnings += (rank * bid)
    return winnings


# Part 2
def p2(hands, bids):
    winnings = 0
    ordered_hands = sorted(hands, key=lambda x: (hands[x], card_strength_2[x[0]], card_strength_2[x[1]], card_strength_2[x[2]], card_strength_2[x[3]], card_strength_2[x[4]]))
    #print(ordered_hands)
    for i in range(len(ordered_hands)):
        rank = i + 1
        bid = bids[ordered_hands[i]]
        winnings += (rank * bid)
    return winnings


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    hands, bids = parse_data(data)
    print("Part 1 Answer: {}".format(p1(hands, bids)))

    hands, bids = parse_data_part2(data)
    print("Part 2 Answer: {}".format(p2(hands, bids)))


if __name__ == "__main__":
    main()
