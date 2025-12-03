def invalid_id(id):
    id = str(id)
    if len(id) % 2 == 1:
        return False
    half = len(id) // 2
    if id[:half] == id[half:]:
        return True
    return False


def p2_invalid(id):
    id = str(id)
    for n in range(2, len(id) + 1):
        rep = 0
        if len(id) % n != 0:
            continue
        seg = len(id) // n
        segments = [id[seg * x : seg * (x + 1)] for x in range(0, n)]
        for y in range(0, len(segments)):
            if segments[0] == segments[y]:
                rep += 1
        if rep == n:
            return True


def process_input(puzzle_input):
    pairs = puzzle_input.split(",")
    ranges = [pair.split("-") for pair in pairs]
    return ranges


def find_doubled_ids(pair):
    invalid_id_list = []
    for x in range(int(pair[0]), int(pair[1]) + 1):
        if invalid_id(x):
            invalid_id_list.append(x)
    return invalid_id_list


def find_patterned_ids(pair):
    invalid_id_list = []
    for x in range(int(pair[0]), int(pair[1]) + 1):
        if p2_invalid(x):
            invalid_id_list.append(x)
    return invalid_id_list


def part_1():
    fake_ids = []
    source = p1_test_input
    ranges = process_input(source)
    for pair in ranges:
        fake_ids += find_doubled_ids(pair)
    print(f"Sum of fake ids in p1 test: {sum(fake_ids)}")
    fake_ids = []
    with open("02_1.txt") as f:
        source = f.read()
    ranges = process_input(source)
    for pair in ranges:
        fake_ids += find_doubled_ids(pair)
    print(f"Sum of fake ids in part one: {sum(fake_ids)}")


def part_2():
    fake_ids = []
    source = p1_test_input
    ranges = process_input(source)
    for pair in ranges:
        fake_ids += find_patterned_ids(pair)
    print(f"Sum of fake ids in p2 test: {sum(fake_ids)}")
    fake_ids = []
    with open("02_1.txt") as f:
        source = f.read()
    ranges = process_input(source)
    for pair in ranges:
        fake_ids += find_patterned_ids(pair)
    print(f"Sum of fake ids in part two: {sum(fake_ids)}")


def main():
    part_1()
    part_2()


p1_test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


if __name__ == "__main__":
    main()
