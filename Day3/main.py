import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
input = [[int(y) for y in x] for x in input]

def part1(input):
    s = 0
    for r in input:
        m = max(r[:-1]) # Don't search the last item, you can't make 2 when the last one is the highest number
        pos_m = r.index(m) 
        m2 = max(r[pos_m+1:]) # Search the rest of the list for the highest number
        num = int(str(m) + str(m2))
        s += num
    return s

def part2(input):
    s = 0
    for r in input:
        parts = 12
        num_str = ""
        for i in range(parts,0,-1):
            if i == 1:
                new_r = r
            else:
                new_r = r[:-i+1]
            m = max(new_r)
            idx = r.index(m)
            for j in range(idx,-1,-1):
                del r[j]
            num_str += str(m)
        s += int(num_str)
    return s
    


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