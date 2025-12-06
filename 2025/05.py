def process_puzzle(path):
    ranges = []
    ids = []
    with open(path, 'r') as f:
        src = f.read()
    rows = src.split('\n')
    for row in rows:
        if len(row) == 0:
            continue
        try:
            ids.append(int(row))
        except:
            ranges.append([int(x) for x in row.split('-')])
    return ranges, ids

def check_fresh(ranges, food_id):
    for row in ranges:
        if food_id < row[0]:
            continue
        if food_id > row[1]:
            continue
        return True
    return False

def find_overlap(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    for r in range(0, len(ranges)-1):
        ranges[r+1][1] = max(ranges[r][1], ranges[r+1][1])
        ranges[r][1] = min(ranges[r][1], ranges[r+1][0]-1)
    return(ranges)


def part1(ranges, ids):
    fresh_foods = 0
    for x in ids:
        if check_fresh(ranges, x):
            fresh_foods += 1
    return fresh_foods

def part2(ranges):
    fresh_ids = 0
    find_overlap(ranges)
    for n in ranges:
        fresh_ids += n[1]-n[0] + 1
    return fresh_ids


fresh_ranges, ingredient_ids = process_puzzle('05_test.txt')
print(f'part1_test: {part1(fresh_ranges, ingredient_ids)}')

fresh_ranges, ingredient_ids = process_puzzle('05.txt')
print(f'part1_real: {part1(fresh_ranges, ingredient_ids)}')

fresh_ranges, ingredient_ids = process_puzzle('05_test.txt')
print(f'part2_test: {part2(fresh_ranges)}')

fresh_ranges, ingredient_ids = process_puzzle('05.txt')
print(f'part2_real: {part2(fresh_ranges)}')

