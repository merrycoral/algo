from collections import deque

def main():

    f = open("C:/algorithm/algo/python/input.txt", 'r')
    #f = sys.stdin

    x = int(f.readline())

    qu = deque()
    for i in range(x):
        #line = input()
        line = f.readline()
        if line[0] == '1' :
            print(line[0], line[1], line[2:], "each char")
            qu.append(line[2:])
        elif line[0] == '2':
            if len(qu) > 0 :
                qu.popleft()
        elif line[0] == '3':
            if len(qu) > 0 :
                print(qu[0])
            else:
                print('-1')
        elif line[0] == '4':
            print(str(len(qu)))

if __name__=="__main__":
    main()