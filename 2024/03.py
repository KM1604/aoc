import re

file_path = "03_input.txt"
mul_pattern = r"mul\((\d+),(\d+)\)"
active_code_pattern = r"do\(\)(.*?)don't\(\)"


def read_day3_file(path):
    commands = ""
    memory_dump = open(file_path)
    for line in memory_dump:
        commands += line
    memory_dump.close()
    return commands


def find_muls(pattern, code):
    sum_product = 0
    muls = re.findall(pattern, code, flags=re.DOTALL)
    for x, y in muls:
        sum_product += int(x) * int(y)
    return sum_product


def clean_code(code):
    active_muls = 0
    active_code_bits = re.findall(active_code_pattern, code, flags=re.DOTALL)
    for x in active_code_bits:
        active_muls += find_muls(mul_pattern, x)
    return active_muls


code = read_day3_file(file_path)
part1_ans = find_muls(mul_pattern, code)
print("part 1 answer:   ", part1_ans)


active_muls = clean_code("do()" + code + "don't()")
print("active muls are: ", active_muls)
