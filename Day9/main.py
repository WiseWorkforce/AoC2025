import os
import timeit
import itertools
from shapely.geometry.polygon import Polygon

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
input = [tuple([int(y) for y in x.split(",")]) for x in input]

def make_combinations(input):
    return itertools.combinations(input, 2)

def calc_area(c):
    c1, c2 = c
    return (abs(c1[0]-c2[0])+1)*(abs(c1[1]-c2[1])+1)

def get_corners(c):
    (w1,h1),(w2,h2) = c
    w1, w2 = sorted([w1, w2])
    h1, h2 = sorted([h1, h2])
    return [(w1+1,h1+1),(w1+1,h2-1),(w2-1,h1+1),(w2-1,h2-1)]

def part1(input):
    combinations = make_combinations(input)
    areas = []
    for c in combinations:
        a = calc_area(c)
        areas.append(a)
    return max(areas)

def part2(input):
    poly = Polygon(input)
    combinations = make_combinations(input)
    comb_with_area = {}
    for c in combinations:
        a = calc_area(c)
        comb_with_area[c] = a
    comb_with_area = dict(sorted(comb_with_area.items(), key=lambda item: item[1],reverse=True))
    for c in comb_with_area.keys():
        corners = get_corners(c)
        square = Polygon(corners)
        if poly.contains(square):
            a = calc_area(c)
            return a

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