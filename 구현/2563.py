import sys

f = sys.stdin

paper = [[0 for _ in range(100)] for _ in range(100)]
    
def colorPaper(x, y) :
    for i in range(x, x+10, 1) :
        if i < 100 :
            for j in range(y, y+10, 1) :
                if j < 100 :
                    paper[i][j] = 1

def findWhite() :
    area = 0
    for row in paper:
        area+= sum(row)
    return area
                
def main():
    n = int(f.readline())
    for _ in range(n) :
        x, y = map(int,f.readline().split(' '))
        colorPaper(x, y)
    print(findWhite())    


if __name__ == "__main__":
    main()
