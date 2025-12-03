class Dial:
    def __init__(self, starting_pos, dial_min, dial_max):
        self.pos = starting_pos
        self.min = dial_min
        self.max = dial_max
        self.tot = dial_max - dial_min + 1

    def rotate(self, rot):
        if rot[0] == "R":
            dir = 1
        elif rot[0] == "L":
            dir = -1
        else:
            dir = 0
        mag = int(rot[1:])
        self.pos = self.pos + (dir * mag)
        self.pos = self.pos % self.tot

    def watch_and_rotate(self, rot):
        zero_clicks = 0
        if rot[0] == "R":
            dir = 1
        elif rot[0] == "L":
            dir = -1
        else:
            dir = 0
        mag = int(rot[1:])
        if dir == 1 and self.pos == 0:
            zero_clicks += 1
        turned = self.pos + (dir * mag)
        while turned < self.min:
            turned += self.tot
            zero_clicks += 1
        while turned > self.tot:
            turned -= self.tot
            zero_clicks += 1
        self.pos = turned % 100
        return zero_clicks


def get_puzzle_source(local_src):
    try:
        with open(local_src, "r") as f:
            document = f.read()
            document = document.split("\n")
            document = document[:-1]
        return document
    except:
        print(f"Did you save input as {local_src}?")
        return False


def part_one():
    Part1_Dial = Dial(50, 0, 99)
    local_source = "01_src.txt"
    target = 0
    pw = 0
    document = get_puzzle_source(local_source)
    for rotation in document:
        Part1_Dial.rotate(rotation)
        # THIS COULD CAUSE PROBLEMS IF WE HAVE AN ERROR LINE AND A REPEATED ZERO
        if Part1_Dial.pos == target:
            pw += 1
    print(f"part one: {pw}")


def part_two():
    Part2_Dial = Dial(50, 0, 99)
    local_source = "01_src.txt"
    pw = 0
    document = get_puzzle_source(local_source)
    for rotation in document:
        pw += Part2_Dial.watch_and_rotate(rotation)
    print(f"part two: {pw}")


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
