def part1(data: str) -> int:
    result = 0
    for line in data.split("\n"):
        _, card_data = line.split(":")
        winning_numbers, your_numbers = [
            [int(number) for number in numbers.strip().split()]
            for numbers in card_data.split("|")
        ]
        exp = len([number for number in your_numbers if number in winning_numbers]) - 1
        partial = 0
        if exp >= 0:
            partial = pow(2, exp)
        result += partial
    return result


def part2(data: str) -> int:
    max_index = len(data.split("\n"))
    cards = [1 for _ in range(max_index)]
    for it, line in enumerate(data.split("\n")):
        _, card_data = line.split(":")
        winning_numbers, your_numbers = [
            [int(number) for number in numbers.strip().split()]
            for numbers in card_data.split("|")
        ]
        for jt in range(
            len([number for number in winning_numbers if number in your_numbers])
        ):
            index = it + jt + 1
            if index < max_index:
                cards[index] += 1 * cards[it]
    return sum(cards)


def main():
    data = None
    with open("day4/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
