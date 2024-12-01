def parse(input):
    data=[[],[]]
    for line in f:
        splits= line.strip().split()
        data[0].append(int(splits[0]))
        data[1].append(int(splits[1]))
    data[0].sort()
    data[1].sort()
    return data

def part1(data):
    return sum(abs(data[0][x]-data[1][x]) for x in range(len(data[0])))

def part2(data):
    return sum(data[0][x]*data[1].count(data[0][x]) for x in range(len(data[0])))

f = open("Day1/input", "r")
data = parse(f)
print(f"Part 1: {part1(data)} ")
print(f"Part 2: {part2(data)} ")