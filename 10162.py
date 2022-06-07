import math
import sys

T = int(sys.stdin.readline())

if (T % 10) != 0 :
    print("-1")
else :
    A = math.floor(T/300)
    B = math.floor((T%300)/60)
    C = math.floor(((T%300)%60)/10)
    print(A, B, C)