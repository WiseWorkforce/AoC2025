import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
input = [[y for y in x] for x in input]

def process_grid(input):
    max_row = len(input) - 1
    max_col = len(input[0]) -1 
    for row_idx,row in enumerate(input):
        for col_idx, val in enumerate(row):
            num = 0
            if val != ".":
                if row_idx > 0 and col_idx > 0:
                    if input[row_idx-1][col_idx-1] != ".": # Col top left
                        num += 1
                if row_idx > 0:
                    if input[row_idx-1][col_idx] != ".": # Col top
                        num += 1 
                if row_idx >0 and col_idx < max_col:
                    if input[row_idx-1][col_idx+1] != ".": # Col top right
                        num += 1 
                if col_idx > 0:
                    if input[row_idx][col_idx-1] != ".": # Col left
                        num += 1 
                if col_idx < max_col:
                    if input[row_idx][col_idx+1] != ".": # Col right
                        num += 1 
                if row_idx < max_row and col_idx > 0:
                    if input[row_idx+1][col_idx-1] != ".": # Col bottom left
                        num += 1 
                if row_idx < max_row:
                    if input[row_idx+1][col_idx] != ".": # Col bottom
                        num += 1 
                if row_idx < max_row and col_idx < max_col:
                    if input[row_idx+1][col_idx+1] != ".": # Col bottom right
                        num += 1 
                input[row_idx][col_idx] = num
    return input

def count_rolls(input):
    s = 0
    for r in input:
        print(len([x for x in r if x != "." and x <4]))
        print(r)
        s += len([x for x in r if x != "." and x <4])
    return s

def replace_rolls(input):
    input_new = []
    for r in input:
        r = list(map(lambda x: "." if x != "." and x < 4 else x, r))
        r = list(map(lambda x: "@" if x != "." else x, r))
        input_new.append(r)
    return input_new

def part1(input):
    o = process_grid(input)
    s = count_rolls(o)
    return s

def part2(input):
    num_roll = 0
    o = process_grid(input)
    s = count_rolls(o)
    num_roll += s
    o = replace_rolls(o)
    while s > 0:
        o = process_grid(o)
        s = count_rolls(o)
        num_roll += s
        o = replace_rolls(o)
    return num_roll
                    



t1 = timeit.default_timer()
p1 = part1(input)
t2 = timeit.default_timer()
print("Part 1: " + str(p1))
print(t2 - t1)
t1 = timeit.default_timer()
#p2 = part2(input)
t2 = timeit.default_timer()
#print("Part 2: " + str(p2))
#print(t2 - t1)
