n = int(input())

time = 0
num = 1

while n > 0:
    if n < num:
        num = 1
    n -= num
    num += 1
    time += 1

print(time)