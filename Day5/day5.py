def parse(input):
    rules, updates = input.read().split("\n\n")
    return [rule.split("|") for rule in rules.split()], [update.split(",") for  update in updates.split()]

def part1(rules, updates):
    sum=0
    for update in updates:
        before=[]
        correct=True
        for page in update:
            for left,right in rules:
                if left==page and right in before:
                    correct=False
            before.append(page)
        if correct:
            sum+=int(update[len(update)//2])
    return sum

def check(update, rules, correct):
    before=[]
    for pageLoc, page in enumerate(update):
        for left,right in rules:
            if left==page and right in before:
                update.remove(right)
                update.insert(pageLoc,right)
                correct=False
        before.append(page)
    if (not correct):
        check(update, rules, True)
    return correct

def part2(rules, updates):
    return sum([int(update[len(update)//2]) for update in updates if (not check(update,rules,True))])

f = open("Day5/input", "r")
rules, updates = parse(f)
print(f"Part 1: {part1(rules, updates)} ")
print(f"Part 2: {part2(rules, updates)} ")