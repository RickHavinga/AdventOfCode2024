import re

pattern=r"mul\((\d{1,3}),(\d{1,3})\)"

def part1(data):
    return sum(int(x)*int(y) for x,y in re.findall(pattern,data))

def part2(data):
    splits = re.split(r"don't\(\)", data)
    total= sum(int(x)*int(y) for x,y in re.findall(pattern,splits[0]))
    for part in splits[1:]:
        splitDo=re.split(r"do\(\)", part)
        for do in splitDo[1:]:
            total+= sum(int(x)*int(y) for x,y in re.findall(pattern,do))
    return total

f = open("Day3/input", "r").readlines()
print(f"Part 1: {part1("".join(f))}")
print(f"Part 2: {part2("".join(f))}")