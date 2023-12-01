from day1.day1 import part1, part2


def test__day1():
    data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    result = part1(data)
    assert result == 142


def test__day2():
    # 29, 83, 13, 24, 42, 14, 76
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    result = part2(data)
    assert result == 281
