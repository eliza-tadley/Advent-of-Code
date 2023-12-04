from collections import defaultdict


def parse_data(data):
    cards = {}
    for card in data:
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        x = card.split(':')
        card_id = int(x[0].split(' ')[-1])
        winning = [int(c.strip()) for c in x[1].strip().split('|')[0].strip().split(' ') if c.isnumeric()]
        hand = [int(c.strip()) for c in x[1].strip().split('|')[1].strip().split(' ') if c.isnumeric()]
        cards[card_id] = (winning, hand)
    return cards


# Part 1
def p1(cards):
    sum_winnings = 0
    for card in cards.values():
        card_winnings = 0
        for num in card[0]:
            if num in card[1]:
                if card_winnings == 0:
                    card_winnings = 1
                else:
                    card_winnings = card_winnings * 2
        sum_winnings += card_winnings
    return sum_winnings


# Part 2
def p2(data):
    num_cards = {}
    for card_id, values in data.items():
        if card_id not in num_cards:
            num_cards[card_id] = 1
        else:
            num_cards[card_id] += 1
        num_current_card = num_cards[card_id]
        matching_numbers = 0
        for num in values[0]:
            if num in values[1]:
                matching_numbers += 1
        for i in range(matching_numbers):
            if card_id + i + 1 in num_cards:
                num_cards[card_id + i + 1] += num_current_card
            else:
                num_cards[card_id + i + 1] = num_current_card
    total = 0
    for c in num_cards.values():
        total += c
    return total



def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    cards = parse_data(data)

    print("Part 1 Answer: {}".format(p1(cards)))
    print("Part 2 Answer: {}".format(p2(cards)))


if __name__ == "__main__":
    main()
