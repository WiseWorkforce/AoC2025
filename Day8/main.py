import os
import timeit
import pandas as pd 
import numpy as np
from scipy.spatial.distance import pdist
import itertools
import math


def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
input = [tuple([int(y) for y in x.split(",")]) for x in input]

def generate_distance_matrix(input):
    combs = list(itertools.combinations(range(len(input)),2))
    coords = []
    for c in combs:
        coords.append((input[c[0]], input[c[1]]))
    df = pd.DataFrame(input, columns=['xcord', 'ycord', 'zcord'])
    x = np.array(input)
    dist = pd.DataFrame(data=pdist(x))
    dist.columns = ["distance"]
    dist['coords'] = coords
    dist['idxs'] = combs
    return dist

def part1(input):
    checks = 1000
    pd.set_option('display.max_rows', None)
    df = generate_distance_matrix(input)
    df = df.sort_values("distance")
    circuits = []
    i = 0
    for r in df.itertuples():
        if i == checks:
            break
        i += 1
        if len(circuits) == 0:
            circuits.append(list(r.idxs))
        else:
            m1 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] in x and r.idxs[1] not in x] # if only first coord in a circuit already
            m2 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] not in x and r.idxs[1] in x] # if only second coord in a circuit already
            m3 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] not in x and r.idxs[1] not in x] # both not in a circuit already
            m4 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] in x and r.idxs[1] in x] # both in a single circuit
            if len(m4) == 0:
                if len(m1) == 0 and len(m2) == 0 and len(m3) == len(circuits):
                    circuits.append(list(r.idxs))
                elif len(m1) > 0 and len(m2) == 0 and len(m3) < len(circuits):
                    circuits[m1[0][0]].append(r.idxs[1])
                elif len(m1) == 0 and len(m2) > 0 and len(m3) < len(circuits):
                    circuits[m2[0][0]].append(r.idxs[0])
                elif len(m1) > 0 and len(m2) > 0 and len(m3) < len(circuits): # both coords exists, but in different circuits, so connect the two
                    c1 = circuits[m1[0][0]]
                    c2 = circuits[m2[0][0]]
                    new_c = c1 + c2
                    circuits.remove(c1)
                    circuits.remove(c2)
                    circuits.append(new_c)
    len_circuits = []
    for c in circuits:
        len_circuits.append(len(c))
    len_circuits.sort(reverse=True)
    return math.prod(len_circuits[:3])

def part2(input):
    pd.set_option('display.max_rows', None)
    df = generate_distance_matrix(input)
    df = df.sort_values("distance")
    num_nodes = len(input)
    circuits = []
    i = 0
    first_junc = input[0]
    for r in df.itertuples():
        if len(circuits) == 0:
            circuits.append(list(r.idxs))
        else:
            m1 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] in x and r.idxs[1] not in x] # if only first coord in a circuit already
            m2 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] not in x and r.idxs[1] in x] # if only second coord in a circuit already
            m3 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] not in x and r.idxs[1] not in x] # both not in a circuit already
            m4 = [(idx,x) for idx,x in enumerate(circuits) if r.idxs[0] in x and r.idxs[1] in x] # both not in a circuit already
            if len(m4) == 0:
                if len(m1) == 0 and len(m2) == 0 and len(m3) == len(circuits):
                    circuits.append(list(r.idxs))
                elif len(m1) > 0 and len(m2) == 0 and len(m3) < len(circuits):
                    circuits[m1[0][0]].append(r.idxs[1])
                elif len(m1) == 0 and len(m2) > 0 and len(m3) < len(circuits):
                    circuits[m2[0][0]].append(r.idxs[0])
                elif len(m1) > 0 and len(m2) > 0 and len(m3) < len(circuits): # both coords exists, but in different circuits, so connect the two
                    c1 = circuits[m1[0][0]]
                    c2 = circuits[m2[0][0]]
                    new_c = c1 + c2
                    circuits.remove(c1)
                    circuits.remove(c2)
                    circuits.append(new_c)
        if len(circuits[0]) == num_nodes:
            last_nodes = r.coords
            break
    return last_nodes[0][0]*last_nodes[1][0]


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