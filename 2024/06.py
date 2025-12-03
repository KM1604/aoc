test_file_path = "06_test_input.txt"
file_path = "06_input.txt"

from aoc06 import classes


class lab_map:
    def __init__(self, path):
        self.floorplan = []
        source_file = open(path, "r")
        for line in source_file:
            self.floorplan.append([x for x in line[:-1]])
        source_file.close()


class guard:
    def __init__(self, lab_map):
        for row in lab_map:
            if "^" in row:
                guard_row = lab_map.index(row)
        guard_col = lab_map[guard_row].index("^")
        guard.start = (guard_row, guard_col)


class pathing:
    def __init__(self, lab, guard):
        pathing.map = lab.floorplan
        pathing.guardloc = guard.start
        pathing.guarddirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        pathing.dir = 0
        pathing.guard_history = []

    def mark_loc(self):
        pathing.map[pathing.guardloc[0]][pathing.guardloc[1]] = "X"

    def record_guard_state(self):
        guarddir = pathing.dir
        guardrow = pathing.guardloc[0]
        guardcol = pathing.guardloc[1]
        guard_state = (guarddir, guardrow, guardcol)
        pathing.guard_history.append(guard_state)
        return guard_state

    def guard_move(self):
        self.mark_loc()
        curr_guard_state = self.record_guard_state()
        if curr_guard_state in pathing.guard_history[:-1]:
            return "loop"
        row = pathing.guardloc[0] + pathing.guarddirs[pathing.dir][0]
        col = pathing.guardloc[1] + pathing.guarddirs[pathing.dir][1]
        if row < 0 or col < 0 or row >= len(pathing.map) or col >= len(pathing.map[0]):
            return "out"
        if pathing.map[row][col] == "#":
            pathing.dir = (pathing.dir + 1) % 4
            row = pathing.guardloc[0] + pathing.guarddirs[pathing.dir][0]
            col = pathing.guardloc[1] + pathing.guarddirs[pathing.dir][1]
        pathing.guardloc = (row, col)
        return True

    def run_simulation(self, map):
        i = True
        while i == True:
            i = self.guard_move()
            if i == "loop":
                return "loop"

    def count_tiles_traveled(self):
        pathing.traveled = 0
        for row in pathing.map:
            pathing.traveled += len([col for col in row if col == "X"])
        print("Guard traveled to this many tiles:", pathing.traveled)

    def check_blocks(self, map):
        possible_loops = 0
        loop_maps = []
        for r in range(0, len(map)):
            for c in range(0, len(map[0])):
                temp_map = [[c for c in r] for r in map]
                temp_map[r][c] = "#"
                if self.run_simulation(temp_map) == "loop":
                    possible_loops += 1
                    loop_maps.append(temp_map)
        return possible_loops, loop_maps


"""
print('Part 1')
test_part1 = lab_map(test_file_path)
test_guard = guard(test_part1.floorplan)
test_map   = pathing(test_part1, test_guard)
test_map.run_simulation(test_map.map)
test_map.count_tiles_traveled()

real_part1 = lab_map(file_path)
real_guard = guard(real_part1.floorplan)
real_map   = pathing(real_part1, real_guard)
real_map.run_simulation(real_map.map)
real_map.count_tiles_traveled()

print('Part 2')
test_part1 = lab_map(test_file_path)
test_guard = guard(test_part1.floorplan)
test_map   = pathing(test_part1, test_guard)
test_num_loops, test_loop_maps = test_map.check_blocks(test_map.map)
print('Possible loops in part 2 test:', test_num_loops)

real_part1 = lab_map(file_path)
real_guard = guard(real_part1.floorplan)
real_map   = pathing(real_part1, real_guard)
real_num_loops, real_loop_maps = real_map.check_blocks(real_map.map)
print('Possible loops in part 2 real:', real_num_loops)
"""

test = classes.guard()
print(test.facing)
