def check_neighbours(data, i: int, j: int, cmp) -> bool:
    data = [[char for char in line] for line in data.split("\n")]
    results = []
    for cors in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ):
        if i + cors[0] < 0 or i + cors[0] > len(data) - 1:
            continue
        if j + cors[1] < 0 or j + cors[1] > len(data[i]) - 1:
            continue
        cell = data[i + cors[0]][j + cors[1]]
        if cmp(cell):
            results.append((i + cors[0], j + cors[1]))

    return len(results) > 0, results


def part1(data: str) -> int:
    parts = []
    for i, line in enumerate(data.split("\n")):
        possible = False
        part_number_buff = ""
        for j, char in enumerate(line):
            if char != "." and char.isdigit():
                part_number_buff += char
                if not possible:
                    possible, _ = check_neighbours(
                        data, i, j, lambda x: x != "." and not x.isdigit()
                    )
            else:
                if possible is True:
                    parts.append(int(part_number_buff))
                possible = False
                part_number_buff = ""
        if len(part_number_buff) > 0 and possible:
            parts.append(int(part_number_buff))
    return sum(parts)


def part2(data: str) -> int:
    stars = {}
    for i, line in enumerate(data.split("\n")):
        possible = False
        cords = []
        part_number_buff = ""
        for j, char in enumerate(line):
            if char != "." and char.isdigit():
                part_number_buff += char
                if possible is not True:
                    possible, cords = check_neighbours(data, i, j, lambda x: x == "*")
            else:
                if possible is True:
                    for c in cords:
                        if c in stars:
                            stars[c].append(part_number_buff)
                        else:
                            stars[c] = [part_number_buff]
                possible = False
                part_number_buff = ""
        if len(part_number_buff) > 0 and possible:
            for c in cords:
                if c in stars:
                    stars[c].append(part_number_buff)
                else:
                    stars[c] = [part_number_buff]
    return sum(
        [
            int(numbers[0]) * int(numbers[1])
            for numbers in stars.values()
            if len(numbers) == 2
        ]
    )


def main():
    data = None
    with open("day3/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
