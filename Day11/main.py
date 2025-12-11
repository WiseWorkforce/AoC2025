import os
import timeit
import functools

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
def process_input(input):
    output = {}
    for x in input:
        k,s = x.split(": ")
        output[k] = []
        for v in s.split(" "):
            output[k].append(v)
    return output
input = process_input(input)

@functools.cache
def next_step(node, fft_in, dac_in):
    p1 = 0
    p2 = 0
    if node == "fft":
        fft_in = True
    elif node == "dac":
        dac_in = True
    for c in input[node]:
        if c == "out" and fft_in and dac_in:
            p1 += 1
            p2 += 1
        elif c == "out":
            p1 += 1
        else:
            new_p1, new_p2 = next_step(c, fft_in, dac_in)
            p1 += new_p1
            p2 += new_p2
    return p1,p2


def part1():
    global counter
    counter = 0
    c = next_step("you",False,False)
    return c[0]

def part2():
    c = next_step("svr",False,False)
    return c[1]
    
t1 = timeit.default_timer()
p1 = part1()
t2 = timeit.default_timer()
print("Part 1: " + str(p1))
print(t2 - t1)
t1 = timeit.default_timer()
p2 = part2()
t2 = timeit.default_timer()
print("Part 2: " + str(p2))
print(t2 - t1)