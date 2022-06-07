import sys

totlen = int(sys.stdin.readline())
num = sys.stdin.readline()

arr = num.split(' ')
arr2 = []

for i in arr : 
    arr2.append(int(i))

# 딸기 초코 바나나 0 1 2
# 1 2 0 2 0 0 1 2 1 1 

temp = 2
milkCount = 0

for i in arr2 :
    if temp == 0 :
        if i == 1 : 
            temp = 1
            milkCount +=1
    elif temp == 1 :
        if i == 2 : 
            temp = 2
            milkCount +=1
    else : 
        if i == 0 : 
            temp = 0
            milkCount +=1

print(milkCount)