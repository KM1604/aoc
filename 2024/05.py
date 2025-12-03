class books:
    def __init__(self, file_path):
        books.input = []
        file = open(file_path, "r")
        for row in file:
            books.input.append(row.replace("\n", ""))
        file.close()
        books.rules = [[int(n) for n in x.split("|")] for x in books.input if "|" in x]
        books.printings = [
            [int(n) for n in x.split(",")] for x in books.input if "," in x
        ]

    def rule_broken(self, printing, rule):
        errors = 0
        try:
            if printing.index(rule[0]) > printing.index(rule[1]):
                errors += 1
        except:
            errors += 0
        return errors != 0

    def rules_followed(self, printing):
        for rule in books.rules:
            if self.rule_broken(printing, rule):
                return False
        return True


########################################################

test = books("05_test_input.txt")

test_rule_followers = []
test_rule_breakers = []
for p in test.printings:
    if test.rules_followed(p):
        test_rule_followers.append(p)
    else:
        test_rule_breakers.append(p)

middle_sum = 0

for p in test_rule_followers:
    middle_sum += p[len(p) // 2]

print("Test part01: ", middle_sum)

live_data = books("05_input.txt")

rule_followers = []
for p in live_data.printings:
    if live_data.rules_followed(p):
        rule_followers.append(p)

middle_sum = 0

for p in rule_followers:
    middle_sum += p[len(p) // 2]

print("Part 01 answer: ", middle_sum)


print("\n\n")
########################################################


class puzzle_source:
    def __init__(self, file_path):
        puzzle_source.input = []
        file = open(file_path, "r")
        for row in file:
            puzzle_source.input.append(row.replace("\n", ""))
        file.close()
        puzzle_source.rules = [
            [int(n) for n in x.split("|")] for x in puzzle_source.input if "|" in x
        ]
        puzzle_source.printings = [
            [int(n) for n in x.split(",")] for x in puzzle_source.input if "," in x
        ]
        puzzle_source.correct_printing = []
        puzzle_source.wrong_printing = []
        for p in puzzle_source.printings:
            if self.rules_broken(p):
                puzzle_source.wrong_printing.append(p)
            else:
                puzzle_source.correct_printing.append(p)

    def rules_broken(self, printing):
        for r in puzzle_source.rules:
            if r[0] not in printing or r[1] not in printing:
                continue
            if printing.index(r[0]) > printing.index(r[1]):
                return True
        return False


def fix_printing(printing, rules):
    working_copy = printing
    for page in working_copy:
        for r in rules:
            if r[0] not in working_copy or page != r[1]:
                continue
            pnum = working_copy.index(page)
            rnum = working_copy.index(r[0])
            if pnum < rnum:
                moved_page = working_copy.pop(pnum)
                working_copy.insert(rnum, moved_page)
                fix_printing(working_copy, rules)
    return working_copy


def fix_printing_list(list, rules):
    ordered_updates = []
    for update in test.wrong_printing:
        fixed = fix_printing(update, test.rules)
        ordered_updates.append(fixed)
    return ordered_updates


def find_middle_pages(updates):
    middle_sum = 0
    for u in updates:
        middle_sum += u[len(u) // 2]
    return middle_sum


test_path = "05_test_input.txt"
real_path = "05_input.txt"

test = puzzle_source(test_path)
test_fixed_list = fix_printing_list(test.wrong_printing, test.rules)
middle_sum_fixed_test = find_middle_pages(test_fixed_list)
print("Part 02 test solution: ", middle_sum_fixed_test)

real = puzzle_source(real_path)
real_fixed_list = fix_printing_list(real.wrong_printing, real.rules)
middle_sum_fixed = find_middle_pages(real_fixed_list)
print("Part 02 real solution: ", middle_sum_fixed)
