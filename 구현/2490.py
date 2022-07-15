import sys
data=[]
f = sys.stdin

while True:
    line = f.readline()
    if not line: break

    data.append(list(line.strip().split(' ')))

def myfunc(data) :
    myDic = {
        0: 'E',
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'
    }
    ans = []

    for i in data:
        count = 0
        for j in i :
            if j == '0' :
                count += 1
        ans.append(myDic[count])
    
    for a in ans :
        print(a)

def main():
    myfunc(data)

if __name__ == "__main__":
    main()