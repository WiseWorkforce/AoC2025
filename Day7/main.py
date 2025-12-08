import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f



def generate_xmas(input):
    start_x = input[0].index("S")
    max_col = len(input[0]) - 1
    input[0][start_x] = "|"
    splitted = 0    
    for r_idx,r in enumerate(input):
        if r_idx > 0:
            for c_idx,c in enumerate(r):
                if input[r_idx-1][c_idx] == "|" and c == ".": # Just go down
                    input[r_idx][c_idx] = "|"
                if input[r_idx-1][c_idx] == "|" and c == "^": # Just go down
                    splitted += 1
                    if c_idx-1>=0:
                        input[r_idx][c_idx-1] = "|"
                    if c_idx+1 <= max_col:
                        input[r_idx][c_idx+1] = "|"
    return (splitted, input, start_x)

def part1(input):
    splitted, input, start_x = generate_xmas(input)
    return splitted


def part2(input):
    splitted, input, start_x = generate_xmas(input)
    max_col = len(input[0])
    o = 1
    empty = []
    for l in input:
        new_row = []
        for c in l:
            new_row.append(0)
        empty.append(new_row)
    empty[0][start_x] = 1
    for r_idx, r in enumerate(input):
        if r_idx > 0:
            for c_idx, c in enumerate(r):
                if c == "|" and input[r_idx-1][c_idx] == "|": # beam, but no splitter above
                    empty[r_idx][c_idx] += empty[r_idx-1][c_idx]
                elif c == "^": # beam, but with splitter
                    if c_idx-1 >= 0:
                        empty[r_idx][c_idx-1] += empty[r_idx-1][c_idx]
                    if c_idx+1 < max_col:
                        empty[r_idx][c_idx+1] += empty[r_idx-1][c_idx]
    return sum(empty[-1])

input = open_file("input.txt")
input = [list(x) for x in input]
t1 = timeit.default_timer()
p1 = part1(input)
t2 = timeit.default_timer()
print("Part 1: " + str(p1))
print(t2 - t1)
input = open_file("input.txt")
input = [list(x) for x in input]
t1 = timeit.default_timer()
p2 = part2(input)
t2 = timeit.default_timer()
print("Part 2: " + str(p2))
print(t2 - t1)