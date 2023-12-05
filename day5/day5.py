def do_work(seeds, chunks):
    for chunk in chunks:
        ranges = []
        for line in chunk.split("\n")[1:]:
            ranges.append(list(map(lambda x: int(x), line.split())))
        for it, seed in enumerate(seeds):
            for r in ranges:
                if r[1] <= seed < r[1] + r[2]:
                    seeds[it] = seed + (r[0] - r[1])
                    break
    return min(seeds)


def part1(data: str) -> int:
    c = data.split("\n\n")
    seeds = [int(seed) for seed in c[0].split(":")[1].strip().split()]
    chunks = c[1:]
    return do_work(seeds, chunks)


def part2(data: str) -> int:
    c = data.split("\n\n")
    seeds_data = [int(seed) for seed in c[0].split(":")[1].strip().split()]
    chunks = c[1:]
    it = 0
    result = None
    while it < len(seeds_data):
        seeds = [_ for _ in range(seeds_data[it], seeds_data[it] + seeds_data[it + 1])]
        tmp = do_work(seeds, chunks)
        if result is None or tmp < result:
            result = tmp
        it += 2

    return result


def main():
    data = None
    with open("day5/input.txt", "r", encoding="utf-8") as input_file:
        data = input_file.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
