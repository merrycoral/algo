import sys

f = sys.stdin

antNum = list(map(int,f.readline().strip().split(' ')))
forward = list(f.readline().strip())
backward = list(f.readline().strip())
time = int(f.readline().strip())

def Jump(antArr):
    changedAnts=[]
    for i in antArr:
        changedAnts.append(i)
    for i in range(len(antArr)-1):
        if antArr[i][1] == 'F' and antArr[i][1] != antArr[i+1][1]:
            changedAnts[i], changedAnts[i+1] = changedAnts[i+1], changedAnts[i]
    return changedAnts

def ants(forward, backward, time) :
    answer= ''
    antArr = []
    for i in range(len(forward)-1, -1, -1):
        antArr.append([forward[i], 'F'])
    for i in backward:
        antArr.append([i, 'B'])

    for _ in range(time) :
        antArr = Jump(antArr)

    for n in antArr:
        answer += n[0]
    print(answer)

ants(forward, backward, time)

