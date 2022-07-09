import sys

f = open("C:/algorithm/python/14471ex.txt", 'r')

lines = f.readlines()
n, m = map(int, lines[0].split())
a = []
for line in lines:
  line = line.strip()
  temp = line.split()
  a.append(int(temp[0]))

#f.close
print(a)

inven = 0
spent = 0

del a[0]
#a.sort(reverse=True)

for i in a :
   if i >= n :
     inven += 1
     a.remove(i)
     
if inven  >= m-1 :
  print(spent)
else :
  a.sort(reverse=True)
  for i in a :
    spent = spent+n-i
    inven += 1
    if inven == m-1 :
      break
  print(spent)