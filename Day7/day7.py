import operator

def concat(value, number):
    return (int(str(value)+str(number)))

def evaluate(numbers, operators):
    values, start =[numbers[0]], 0
    for number in numbers[1:]:
        for i in range(start,len(values)):
            for operator in operators:
                values.append(operator(values[i],number))
            start=i
    return values

def calibrationResult(equations, operators):
    return sum(testValue for testValue, numbers in equations if testValue in evaluate(numbers, operators))

f = open("Day7/input", "r")
equations = [(int(eq.split(':')[0]), list(map(int,eq.split(':')[1].split()))) for eq in f.readlines()]
print(f"Part 1: {calibrationResult(equations, [operator.mul, operator.add])} ")
print(f"Part 2: {calibrationResult(equations, [operator.mul, operator.add, concat])} ")