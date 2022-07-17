import sys

f = open("C:/algorithm/algo/구현/input.txt", 'r')
#f = sys.stdin

initInfo = list(f.readline().strip().split(' '))
xDic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
xReverse = {v:k for k,v in xDic.items()}
n = int(initInfo[2])

dirArr = []
for i in range(n) :
    dirArr.append(f.readline().strip())

def moveFunc(pos, direction):
   
    x = pos[0]
    y = pos[1]
    dxy = {
        'R' : (x + 1, y), 'L' : (x - 1, y),
        'T' : (x, y + 1), 'B' : (x, y - 1),
        'RT' : (x + 1, y + 1), 'RB' : (x + 1, y - 1),
        'LB' : (x - 1, y - 1), 'LT' : (x - 1, y + 1)
    }

    if dxy[direction][0] > 8 or dxy[direction][0] < 1 :
        return pos
    elif dxy[direction][1] > 8 or dxy[direction][1] < 1 :
        return pos

    return dxy[direction]

def shallIMove(kpos, spos, d):
    mkpos = moveFunc(kpos, d)
    if mkpos == spos : 
        mspos = moveFunc(spos, d)
        if spos == mspos : 
            return [kpos, spos]
        return [mkpos, mspos]
    return [mkpos, spos]

def main():
    kpos = (int(xDic[initInfo[0][0]]), int(initInfo[0][1]))
    spos = (int(xDic[initInfo[1][0]]), int(initInfo[1][1]))

    for d in dirArr :
        temp = shallIMove(kpos, spos, d)
        kpos = temp[0]
        spos = temp[1]

    print(xReverse[kpos[0]], kpos[1], sep='')
    print(xReverse[spos[0]], spos[1], sep='')
    
if __name__ == "__main__":
    main()

