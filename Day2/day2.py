def parse(input):
    return [[int(level) for level in line.split()] for line in input]

def isSafe(report):
    return (all(1<=report[level]-report[level-1]<=3 for level in range(1,len(report))) or
            all(1<=report[level-1]-report[level]<=3 for level in range(1,len(report)))) 

def part1(data):
    return sum(isSafe(report) for report in data)

def part2(data):
    return sum(isSafe(report) or any(isSafe(report[:i]+report[i+1:]) for i in range(len(report))) for report in data)

f = open("Day2/input", "r")
data = parse(f)
print(f"Part 1: {part1(data)} ")
print(f"Part 2: {part2(data)} ")