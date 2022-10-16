import sys

f = open("C:/algorithm/algo/구현/input.txt", 'r')
#f = sys.stdin

data = []

n, m = list(f.readline().split(' '))
while True:
    line = f.readline()
    if not line: break
    data.append(list(line.strip()))

maxEachLine = []    
for i in data :
    for j in data[i] :
        maxEachLine.append(max(data[i]))
        
target = max(maxEachLine)

for a in maxEachLine :
    if a == target :
        print('do')

def findMaxSum(index) :
    sum = data[index[0][index[1]]]
    #index [1, 2]
    around = []
    around.append(data[index[0]-1][index[1]-1])
    around.append(data[index[0]-1][index[1]+1])
    around.append(data[index[0]-1][index[1]-1])
        
        
#이거는 DFS를 써야할 것 같다.