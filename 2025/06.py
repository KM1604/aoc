def process_puzzle(path):
    with open(path) as f:
        src = f.read()
    src = src.split('\n')[:-1]
    return src

def part1(src):
    print(src)
    
src = process_puzzle('06_test.txt')
part1(src)

print(int(' 4'))
