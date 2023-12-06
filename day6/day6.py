from typing import List, Tuple


def do_work(data: List[Tuple[int]]) -> int:
    results = []
    for race_data in data:
        counter = 0
        for t in range(race_data[0] + 1):
            if t * (race_data[0] - t) > race_data[1]:
                counter += 1
        results.append(counter)
    res = 1
    for r in results:
        res *= r
    return res


def part1(data: str) -> int:
    data = list(
        zip(
            *[
                [int(value) for value in data_line.split(":")[1].strip().split()]
                for data_line in data.split("\n")
            ]
        )
    )
    return do_work(data)


def part2(data: str) -> int:
    data = [
        [
            int("".join([value for value in data_line.split(":")[1].strip().split()]))
            for data_line in data.split("\n")
        ]
    ]
    return do_work(data)


def main():
    data = None
    with open("day6/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
