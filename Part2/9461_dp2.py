import sys
#f = sys.stdin
f = open("C:/algorithm/algo/구현/input.txt", 'r')

padovan = [0] *101
padovan[1], padovan[2], padovan[3] = 1, 1, 1

for n in range(1,98):
	padovan[n+3] = padovan[n]+padovan[n+1]

T = int(f.readline())
for i in range(T) :
	k = int(f.readline())
	print(padovan[k])

