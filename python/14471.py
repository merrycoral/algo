import sys

f = open("C:/algorithm/python/14471ex.txt", 'r')
#a, b = map(int, sys.stdin.readline().split())

lines = f.readlines()
f.close
#n, m = map(int, lines[0].split())
a = []
b = []
#temp= list(map(str, sys.stdin.readlines()))
temp= list(map(str, lines))
for i in temp :
  a.append(int(i.split()[0]))
  b.append(int(i.split()[1]))
n = a[0]
m = b[0]
# print(b)

inven = 0
spent = 0

del a[0]
#a.sort(reverse=True)

fail = []

for i in a :
  if i >= n :
     inven += 1
  else: 
    fail.append(i)
     
if inven  >= m-1 :
  print(spent)
else :
  fail.sort(reverse=True)
  for i in fail :
    spent = spent+n-i
    inven += 1
    if inven == m-1 :
      print(spent)
      break
    #print(spent)