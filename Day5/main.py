import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n\n")
    return f

input = open_file("input.txt")
input = [x.split("\n") for x in input]

def part1(input):
    rngs, ingredients = input
    rngs = [[int(y) for y in x.split("-")] for x in rngs]
    rngs = [range(x[0],x[1]+1) for x in rngs]
    ingredients = [int(x) for x in ingredients]
    valid_ids = []
    for i in ingredients:
        if i not in valid_ids:
            for j in rngs:
                if i in j:
                    valid_ids.append(j)
                    break
    return len(valid_ids)

def part2(input):
    rngs = [[int(y) for y in x.split("-")] for x in input[0]]
    rngs = sorted(rngs, key=lambda x: (x[0], x[1]))
    # Check for overlapping ranges
    for i in range(len(rngs)-1,0,-1):
        remove = False
        cur = rngs[i]
        prev = rngs[i-1]
        if prev[1] >= cur[0] and prev[1] <= cur[1]: # Within range
            rngs[i-1][1] = cur[1]
            remove = True
        if prev[0] <= cur[0] and prev[1] >= cur[1]: # prev fully "over" current, delete current
            remove = True
        if remove:
            del rngs[i]
    c = 0 
    for i in rngs:
        c += i[1] - i[0] + 1
    return c

t1 = timeit.default_timer()
p1 = part1(input)
t2 = timeit.default_timer()
print("Part 1: " + str(p1))
print(t2 - t1)
t1 = timeit.default_timer()
p2 = part2(input)
t2 = timeit.default_timer()
print("Part 2: " + str(p2))
print(t2 - t1)