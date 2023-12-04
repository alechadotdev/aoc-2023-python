CHECK = {"red": 12, "green": 13, "blue": 14}


def part1(data: str) -> int:
    result = 0
    for game in data.split("\n"):
        game_id, game_data = game.split(":")
        possible_game = True
        for attempt in game_data.split(";"):
            for attempt_data in attempt.split(","):
                value, cube_color = attempt_data.strip().split(" ")
                if int(value) > CHECK[cube_color]:
                    possible_game = False
                    break
        if possible_game:
            game_id = game_id.split(" ")[1]
            result += int(game_id)
    return result


def part2(data: str) -> int:
    result = 0
    for game in data.split("\n"):
        game_id, game_data = game.split(":")
        possible_game = True
        attempt_max = {"red": 0, "green": 0, "blue": 0}
        for attempt in game_data.split(";"):
            for attempt_data in attempt.split(","):
                value, cube_color = attempt_data.strip().split(" ")
                if int(value) > attempt_max[cube_color]:
                    attempt_max[cube_color] = int(value)
        result += attempt_max["red"] * attempt_max["green"] * attempt_max["blue"]
    return result


def main():
    data = None
    with open("day2/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
