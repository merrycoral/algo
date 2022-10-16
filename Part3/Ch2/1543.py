doc = input()
target = input()
n = len(target)
t = len(doc)
ans = 0

if n == t:
    if doc == target:
        print(1)
else:
    for i in range(1, t-n) :
        print(doc[-i-n:-i])
        if doc[-i-n:-i] == target:
            ans += 1
            i +=n
        else:
            i +=1

    print(ans)