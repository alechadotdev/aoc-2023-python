from collections import Counter
from enum import IntEnum


class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


def get_hand_type(cards):
    counter = Counter(cards)
    counter_values = [v for v in counter.values()]
    if 5 in counter_values:
        return HandType.FIVE_OF_A_KIND, max(counter, key=counter.get)
    if 4 in counter_values:
        return HandType.FOUR_OF_A_KIND, max(counter, key=counter.get)
    if 3 in counter_values:
        return HandType.THREE_OF_A_KIND, max(counter, key=counter.get)
    if counter_values.count(2) == 2:
        return HandType.TWO_PAIRS, max(counter, key=counter.get)
    if 2 in counter_values:
        return HandType.ONE_PAIR, max(counter, key=counter.get)
    if len(counter) == 5:
        return HandType.HIGH_CARD, max(counter, key=counter.get)


def cards_to_int(cards):
    for card in cards:
        if card == "T":
            yield 10
        elif card == "J":
            yield 11
        elif card == "Q":
            yield 12
        elif card == "K":
            yield 13
        elif card == "A":
            yield 14
        else:
            yield int(card)


def part1(data: str) -> int:
    hands = data.split("\n")
    d = []
    for hand in hands:
        cards, bid = hand.split()
        cards = list(cards_to_int(cards))
        hand_type, best_card = get_hand_type(cards)
        d.append([best_card, bid, hand_type])
    d.sort(key=lambda x: (x[2], x[0]))
    return sum([(it + 1) * int(x[1]) for it, x in enumerate(d)])


def part2(data: str) -> int:
    return 0


def main():
    data = None
    with open("day7/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
