import sys
from tkinter.tix import Tree
f = open("C:/algorithm/algo/BFSDFS/input2.txt", 'r')
#f = sys.stdin

n = int(f.readline())
area = []



def solve(rain):

    def dfs(x, y):
        if x <=-1 or x >= n or y <=-1 or y >= n :
            return False
        if temparr[x][y] != 0:
            temparr[x][y] == 0

            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
        return False
    
    count = 0
    temparr = area.copy()
    for i in temparr :
        for j in i:
            if j <= rain :
                j = 0
    for i in range(n) :
        for j in range(n):
            if dfs(i, j) == True:
                count +=1        
    return count

def main():
    for i in range(n) :
        line = f.readline()
        a = list(map(int, line.split(' ')))
        area.append(a)

    numberOfWater = []
    for rain in range(1, 9):
        numberOfWater.append(solve(rain))        
    print(max(numberOfWater))

if __name__ == "__main__":
    main()
