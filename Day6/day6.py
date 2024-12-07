def parse(input):
    matrix={}
    start=()
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if (char=='^'):
                start=(x,y)
                matrix[(x,y)]=True
            elif(char=='#'):
                matrix[(x,y)]=False
            else:
                matrix[(x,y)]=True
            w=x
        h=y
    return matrix, start, h, w

def part1(matrix, start):
    dirs={0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
    i=0
    visited=set()
    loc=start
    inMatrix=True
    while inMatrix:
        visited.add(loc)
        nextLoc=(loc[0]+dirs[i%4][0], loc[1]+dirs[i%4][1])
        if(nextLoc in matrix):
            if (matrix[nextLoc]):
                loc=nextLoc
            else:
                i+=1
        else:
            inMatrix=False
    return len(visited)
    
def check(matrix, start):    
    dirs={0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
    i=0
    visited=set()
    loc=start
    inMatrix=True
    while inMatrix:
        nextLoc=(loc[0]+dirs[i%4][0], loc[1]+dirs[i%4][1])
        if ((loc,dirs[i%4]) in visited):
            return True
        visited.add((loc,dirs[i%4]))
        if(nextLoc in matrix):
            if (matrix[nextLoc]):
                loc=nextLoc
            else:
                i+=1
        else:
            inMatrix=False
    return False

def part2(matrix, start, h, w):
    count=0
    for y in range(h+1):
        for x in range(w+1):
            if (matrix[(x,y)]):
                tmpMatrix=matrix.copy()
                tmpMatrix[(x,y)]=False
                if (check(tmpMatrix, start)):
                    count+=1
    return count

f = open("Day6/input", "r")
matrix, start, h, w = parse(f)
print(f"Part 1: {part1(matrix, start)} ")
print(f"Part 2: {part2(matrix, start, h, w)} ")