# file_path = '04_test_input.txt'
file_path = "04_input.txt"
word = "XMAS"


def read_file(path):
    word_search = []
    input_file = open(file_path, "r")
    for line in input_file:
        word_search.append([c for c in line if c != "\n"])
    input_file.close()
    return word_search


def find_word(puzzle, word, column, row, dx, dy):
    found_word = ""
    for c in range(0, len(word)):
        if row + dy * c < 0 or column + dx * c < 0:
            continue
        try:
            found_word += puzzle[row + dy * c][column + dx * c]
        except:
            continue
    if found_word == word:
        return True
    else:
        return False


def find_word_any_direction(puzzle, word, column, row):
    n = 0
    if find_word(puzzle, word, column, row, -1, 1):
        n += 1
    if find_word(puzzle, word, column, row, 0, 1):
        n += 1
    if find_word(puzzle, word, column, row, 1, 1):
        n += 1
    if find_word(puzzle, word, column, row, -1, 0):
        n += 1
    if find_word(puzzle, word, column, row, 1, 0):
        n += 1
    if find_word(puzzle, word, column, row, -1, -1):
        n += 1
    if find_word(puzzle, word, column, row, 0, -1):
        n += 1
    if find_word(puzzle, word, column, row, 1, -1):
        n += 1
    return n


def find_all(puzzle, word):
    puzzle_matches = 0
    for r in range(0, len(puzzle)):
        for c in range(0, len(puzzle[r])):
            current_matches = find_word_any_direction(puzzle, word, c, r)
            puzzle_matches += current_matches
        r += 1
    return puzzle_matches


puzzle = read_file(file_path)

puzzle_matches = find_all(puzzle, word)
print("total matches equal: ", puzzle_matches)


def xmas_search(puzzle, r, c):
    if c == 0 or r == 0:
        return 0
    if c == len(puzzle[r]) - 1:
        return 0
    if r == len(puzzle) - 1:
        return 0
    loc0 = puzzle[r][c]
    loc1 = puzzle[r + 1][c + 1]
    loc2 = puzzle[r - 1][c + 1]
    loc3 = puzzle[r - 1][c - 1]
    loc4 = puzzle[r + 1][c - 1]
    if (
        loc0 != "A"
        or loc1 not in "MS"
        or loc2 not in "MS"
        or loc3 not in "MS"
        or loc4 not in "MS"
    ):
        return 0
    if loc1 == loc3:
        return 0
    if loc2 == loc4:
        return 0
    return 1


def find_x_mas(puzzle):
    matches = 0
    for r in range(0, len(puzzle)):
        for c in range(0, len(puzzle[0])):
            matches += xmas_search(puzzle, r, c)
    return matches


solution = find_x_mas(puzzle)
print('cross "MAS" patterns found: ', solution)
