def input_loads(puzzle_text):
    rows = puzzle_text.split("\n")
    rows = [row for row in rows if len(row) > 0]
    list_grid = []
    for row in rows:
        list_grid.append([n for n in row])
    return list_grid


def find_adjacent(src, y, x, n):
    n_count = 0
    for row in range(y - 1, y + 2):
        for col in range(x - 1, x + 2):
            if row < 0 or col < 0:
                continue
            elif row == y and col == x:
                continue
            try:
                if src[row][col] == n and (row != y or col != x):
                    n_count += 1
            except:
                n_count += 0
    return n_count


def n_count(src, n):
    accessible = 0
    for x in range(0, len(src[0])):
        for y in range(0, len(src)):
            if src[y][x] != n:
                continue
            adjacent = find_adjacent(src, y, x, "@")
            if adjacent < 4:
                accessible += 1
    return accessible


def remove_paper(src, n):
    removed = 0
    for x in range(0, len(src[0])):
        for y in range(0, len(src)):
            if src[y][x] != n:
                continue
            adjacent = find_adjacent(src, y, x, "@")
            if adjacent < 4:
                removed += 1
                src[y][x] = "."
    return removed


def remove_all_paper(src, n):
    removed = -1
    total_removed = 0
    while removed != 0:
        removed = remove_paper(src, n)
        total_removed += removed
    return total_removed


with open("04_test.txt") as f:
    text = f.read()
test = input_loads(text)

part1_test = n_count(test, "@")
print(f"part1 test: {part1_test}")

with open("04.txt") as f:
    text = f.read()
puzzle = input_loads(text)

part1_real = n_count(puzzle, "@")
print(f"part1 real: {part1_real}")

part2_test = remove_all_paper(test, "@")
print(f"part2 test: {part2_test}")

part2_real = remove_all_paper(puzzle, "@")
print(f"part2 real: {part2_real}")
