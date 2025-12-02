import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read()
    return f

input = open_file("input.txt")
input = [[int(y) for y in x.split("-")] for x in input.split(",")]

def part1(input):
    invalid = 0
    for x in input:
        f,t = x
        for i in range(f,t + 1):
            s = str(i)
            h = len(s)
            if h % 2 == 0:
                if s[:h//2] == s[h//2:]:
                    invalid += i
    return invalid

def part2(input):
    invalid = 0
    for x in input:
        f,t = x
        for i in range(f,t + 1):
            s = str(i)
            r = s in (s + s)[1:-1]
            if r:
                invalid += i
    return invalid


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