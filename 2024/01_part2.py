# Code for day one, part one of the 2024 advent of code
input_filename = "01_input.txt"


def read_file(file):
    first_list = []
    second_list = []
    for line in input:
        values = line.split("   ")
        first_list.append(int(values[0]))
        second_list.append(int(values[1]))
    return first_list, second_list


def compare_sorted_lists(first, second):
    diff = 0
    for x, y in zip(sorted(first), sorted(second)):
        diff += abs(y - x)
    return diff


def similarity_score(left, right):
    similarity_score = 0
    for location in left:
        similarity_score += location * len([r for r in right if r == location])
    return similarity_score


input = open(input_filename, "r")
first_list, second_list = read_file(input)
input.close()

list_difference = compare_sorted_lists(first_list, second_list)
print("The distance between the lists is:", list_difference)

s_score = similarity_score(first_list, second_list)
print("The similarity score is:", s_score)
