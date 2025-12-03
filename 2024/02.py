# reminder: install regex if you haven't already, dumbass.

import regex
import requests

file_path = "02_input.txt"


def read_file(path):
    lines = []
    contents = open(path)
    for line in contents:
        string_list = line[:-1].split(" ")
        int_list = [int(x) for x in string_list]
        lines.append(int_list)
    return lines


def safe_report(report):
    changes = []
    i = 0
    for level in range(0, len(report) - 1):
        change = report[i + 1] - report[i]
        changes.append(change)
        i += 1
    if sum([abs(x) for x in changes if abs(x) > 3 or x == 0]):
        return "unsafe"
    elif len([x for x in changes if x > 0]) < len(changes) and len(
        [x for x in changes if x < 0]
    ) < len(changes):
        return "unsafe"
    else:
        return "safe"


report_list = read_file(file_path)

safe_reports = 0
unsafe_reports = 0
for report in report_list:
    if safe_report(report) == "safe":
        safe_reports += 1
    else:
        unsafe_reports += 1
print("undampened safe reports:  ", safe_reports)
print("undampened unsafe reports:", unsafe_reports)


def prob_dampener(report):
    n = 0
    for x in range(0, len(report)):
        new_report = report_less_one(report, n)
        if safe_report(new_report) == "safe":
            return "safe"
        n += 1


def report_less_one(report, n):
    report_less = []
    i = 0
    for x in range(0, len(report)):
        if i != n:
            report_less.append(report[i])
        i += 1
    return report_less


damp_safe_reports = 0
damp_unsafe_reports = 0
for report in report_list:
    if prob_dampener(report) == "safe":
        damp_safe_reports += 1
    else:
        damp_unsafe_reports += 1
print("dampened safe reports:    ", damp_safe_reports)
print("dampened unsafe reports:  ", damp_unsafe_reports)
