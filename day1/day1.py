from typing import List

MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def part1(data: str) -> int:
    return sum(
        [
            (lambda x: int(f"{x[0]}{x[-1]}"))(
                [value for value in line if value.isdigit()]
            )
            for line in data.split("\n")
        ]
    )

def find_first_digit(line: str) -> int:
    for it, char in enumerate(line): 
        if char.isdigit():
            return char
        for key in MAPPING:
            if line[it:].startswith(key):
                return MAPPING[key]

def find_last_digit(line: str) -> int:
    line = line[::-1]
    for it, char in enumerate(line):
        if char.isdigit():
            return char
        for key in MAPPING:
            if line[it:].startswith(key[::-1]):
                return MAPPING[key]

def part2(data: str) -> int:
    return sum([int(f"{find_first_digit(line)}{find_last_digit(line)}") for line in data.split("\n")])
        


def main():
    input_data = None
    with open("day1/input.txt", "r", encoding="utf-8") as input_file:
        input_data = input_file.read()
    print(part1(input_data))
    print(part2(input_data))


if __name__ == "__main__":
    main()
