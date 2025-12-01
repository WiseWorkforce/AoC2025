import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
#input = [int(x) for x in input]

def process_input(input):
    return [(x[0],int(x[1:])) for x in input]

def part1(input):
    pos = 50
    zeroes = 0
    input = process_input(input)
    for x in input:
        direction, steps = x
        if len(str(steps)) > 2:
            steps = int(str(steps)[-2:])
        if direction == "L":
            pos = pos - steps
            if pos < 0:
                pos = 100 + pos
        elif direction == "R":
            pos = pos + steps
            if pos > 99:
                pos = pos - 100
        if pos == 0:
            zeroes += 1
    return zeroes

def part2(input):
    pos = 50
    zeroes = 0
    input = process_input(input)
    for x in input:
        direction, steps = x
        prefix = 0
        if len(str(steps)) > 2:
            prefix = int(str(steps)[0:-2])
            steps = int(str(steps)[-2:])
        if direction == "L":
            if steps > pos and pos != 0: # going past zero once or landed on zero
                zeroes += 1
            pos = pos - steps
            if pos < 0:
                pos = 100 + pos  
        elif direction == "R":
            pos = pos + steps
            if pos > 100:
                zeroes += 1
            if pos > 99:
                pos = pos - 100
        if pos == 0:
            zeroes += 1
        zeroes += prefix
    return zeroes


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