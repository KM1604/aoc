part1_test = """987654321111111
811111111111119
234234234234278
818181911112111"""

part1_path = "03.txt"


def max_joltage(row):
    if len(row) < 2:
        return 0
    batteries = [int(x) for x in row]
    first = max(batteries[:-1])
    second = max(batteries[batteries.index(first) + 1 :])
    return first * 10 + second


def part1(src):
    total_joltage = 0
    rows = src.split("\n")
    for row in rows:
        total_joltage += max_joltage(row)
    return total_joltage


def best_batteries(batteries: list, num_left: int):
    if len(batteries) == 0:
        return 0
    if num_left == 1:
        available = batteries
    else:
        available = batteries[: -num_left + 1]
    most_joltage = max(available)
    loc = batteries.index(most_joltage)
    num_left -= 1
    power = most_joltage * 10 ** (num_left)
    if num_left > 0:
        power += best_batteries(batteries[loc + 1 :], num_left)
    return power


def part2(src, num_batteries):
    rows = src.split("\n")
    total_power = 0
    for row in rows:
        batteries = [int(x) for x in row]
        total_power += best_batteries(batteries, num_batteries)
    return total_power


def main():
    print(f"part1 test: {part1(part1_test)}")
    with open(part1_path) as f:
        src = f.read()
    print(f"part1 real: {part1(src)}")
    print(f"part2 test: {part2(part1_test,12)}")
    with open(part1_path) as f:
        src = f.read()
    print(f"part2 real: {part2(src,12)}")


if __name__ == "__main__":
    main()
