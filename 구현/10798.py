import sys
data=[]

f = sys.stdin
while True:
    line = f.readline()
    if not line: break
    data.append(list(line.strip()))

def sero(data) :
    max_length = 0
    for s in data :
        if len(s) > max_length:
            max_length = len(s)

    ans = ''
    for j in range(max_length):
        for i in range(len(data)):
            try:
                if data[i][j] != '' :
                    ans += data[i][j]
            except:
                continue

    return ans

def main():
    print(sero(data))


if __name__ == "__main__":
    main()