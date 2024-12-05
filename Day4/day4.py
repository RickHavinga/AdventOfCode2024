def parse(input):
    matrix={}
    for y, line in enumerate(input):
        for x, char in enumerate(line.strip()):
            matrix[(x,y)]=char
    return matrix

def part1(matrix):
    dirs=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    count=0
    for x,y in matrix:
        if matrix[x,y] == 'X':
            for dir in dirs:
                if ''.join([matrix[coord] for i in range(1,4) if (coord:=(x+dir[0]*i,y+dir[1]*i)) in matrix]) == "MAS":
                    count+=1
    return count

def part2(matrix):
    dirs=[[(-1,1),(1,-1)],[(1,1),(-1,-1)]]
    count=0
    for x,y in matrix:
        if (matrix[x,y]=='A'):
            words=[]
            for dir in dirs:
                if (word:=''.join([matrix[coord] for i in dir if (coord:=(x+i[0],y+i[1])) in matrix]) in ["SM" ,"MS"]):
                    words.append(word)
            if (len(words)==2):
                count+=1
    return count

f = open("Day4/input", "r").readlines()
puzzel = parse(f)
print(f"Part 1: {part1(puzzel)} ")
print(f"Part 2: {part2(puzzel)} ")