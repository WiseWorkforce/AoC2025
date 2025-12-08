import os
import timeit

def open_file(filename):
    d = os.path.dirname(os.path.realpath(__file__))
    f = open(d + "/" + filename)
    f = f.read().split("\n")
    return f

input = open_file("input.txt")
#input = [int(x) for x in input]

def part1(input):
    return_val = 0
    operators = [x for x in input[-1:][0].split(" ") if x != ""]
    nums = []
    for i in range(0,len(input)-1):
        line = [int(x) for x in input[i].split(" ") if x != ""]
        nums.append(line)
    for i in range(0, len(nums[0])):
        operator = operators[i]
        calc_str = ""
        for j in range(0,len(nums)):
            num = nums[j][i]
            calc_str += str(num) + operator
        return_val += eval(calc_str[:-1])
    return return_val

def part2(input):
    operators = [x for x in input[-1:][0].split(" ") if x != ""]
    operators = operators[::-1]
    nums = []
    for i in range(0,len(input)-1):
        rev = input[i][::-1] # reverse the string
        line = list(rev)
        nums.append(line)
    transposed = list(zip(*nums))
    operator_idx = 0
    calc_strs = []
    calc_str = ""
    for t in transposed:
        s = "".join(t)
        s = s.strip()
        if len(s) > 0:
            s = int(s)
            calc_str += str(s) + operators[operator_idx]
        elif len(s) == 0:
            operator_idx += 1
            calc_strs.append(calc_str[:-1])
            calc_str = ""
    operator_idx += 1
    calc_strs.append(calc_str[:-1])
    calc_str = ""
    return_val = 0
    for c in calc_strs:
        return_val += eval(c)
    return return_val

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