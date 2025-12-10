import os
import timeit
import itertools
from scipy.optimize import linprog

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f


input = open_file("input.txt")
input = [(x[0:x.find("]")+1].replace("]","").replace("[",""),eval(x[x.find("]")+2:x.find(") {")+1].replace(" ",",")),eval(x[x.find("{"):].replace("}","").replace("{","")))  for x in input]

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        if isinstance(row,int):
            row = (row,)
        flat_list.extend(row)
    return flat_list

def get_minimum_button_presses(lights,wiring):
    for l in range(1,len(wiring)+1):
        combos = itertools.combinations(wiring, l)
        for c in combos:
            new_wiring = [False for _ in range(len(lights))] #reset the wiring to all off
            for press in c:
                if isinstance(press,int):
                    press = (press,)
                new_wiring = [x^True if idx in press else x for idx,x in enumerate(new_wiring)]
            new_wiring = ''.join(["#" if x else "." for x in new_wiring])
            if lights == new_wiring:
                return l
            
def get_minimum_presses_joltage(wiring, joltage):
    wiring = tuple([(x,) if isinstance(x,int) else x for x in wiring])
    matrix = [[i in b for b in wiring] for i in range(len(joltage))]
    res = linprog([1]*len(wiring), A_eq=matrix, b_eq=joltage, integrality=1)
    return sum(res.x)

def part1(input):
    presses = 0
    for lights,wiring,joltage in input:
        presses += get_minimum_button_presses(lights,wiring)
        break
    return presses

def part2(input):
    presses = 0
    for lights,wiring,joltage in input:
        p = get_minimum_presses_joltage(wiring,joltage)
        presses += p
    return int(presses)

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