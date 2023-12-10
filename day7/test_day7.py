from day7.day7 import part1, part2


def test_part1():
    data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    result = part1(data)
    assert result == 6440


def test_part2():
    data = """"""
    result = part2(data)
    assert result == 0
