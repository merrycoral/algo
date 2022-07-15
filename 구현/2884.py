import sys

f = sys.stdin

time = list(map(int,f.readline().strip().split(' ')))

def minus45(time) :
    convertedTime = [0, 0]
    convertedTime[0] = time[0] -1
    convertedTime[1] = time[1] +15
    if convertedTime[1] >= 60 :
        convertedTime[1] -= 60
        convertedTime[0] += 1

    if convertedTime[0] >= 24 :
        convertedTime[0] -= 24
    elif convertedTime[0] < 0 :
        convertedTime[0] += 24

    print(convertedTime[0], convertedTime[1])

minus45(time)