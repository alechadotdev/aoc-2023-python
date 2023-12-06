from day6.day6 import part1, part2


def test_part1():
    data = """Time:      7  15   30
Distance:  9  40  200"""
    result = part1(data)
    assert result == 288


def test_part2():
    data = """Time:      7  15   30
Distance:  9  40  200"""
    result = part2(data)
    assert result == 71503
