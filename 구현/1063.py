import sys

f = sys.stdin

initInfo = list(f.readline().strip().split(' '))
xDic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'G': 9}
xReverse = {v:k for k,v in xDic.items()}
n = int(initInfo[2])

dirArr = []
for i in range(n) :
    dirArr.append(f.readline().strip())

def moveFunc(pos, direction):
    memo = [pos[0], pos[1]]
    if direction  == 'T' :
        pos[0] += 1
    elif direction == 'B' :
        pos[0] -= 1
    elif direction  == 'R' :
        pos[1] += 1
    elif direction == 'L' :
        pos[1] -= 1
    elif direction  == 'RT' :
        pos[0] += 1
        pos[1] += 1
    elif direction == 'RB' :
        pos[0] -= 1
        pos[1] += 1
    elif direction  == 'LT' :
        pos[0] += 1
        pos[1] -= 1
    elif direction == 'LB' :
        pos[0] -= 1
        pos[1] -= 1

    if pos[0] > 9 or pos[0] < 1 :
        return memo
    elif pos[1] > 9 or pos[1] < 1 :
        return memo

    return pos

def main():
    kpos = [int(xDic[initInfo[0][0]]), int(initInfo[0][1])]
    spos = [int(xDic[initInfo[1][0]]), int(initInfo[1][1])]

    for d in dirArr :
        kpos = moveFunc(kpos, d)
        if kpos == spos : 
            spos = moveFunc(spos, d)

    print(xReverse[kpos[0]], kpos[1], sep='')
    print(xReverse[spos[0]], spos[1], sep='')
    
if __name__ == "__main__":
    main()

