import sys

a=[]
temp= list(map(str, sys.stdin.readlines()))
for i in temp :
  if i == 0:
    m = int(i.split()[0])
  a.append(int(i.split()[0]))
  
n = a[0]
m = b[0]

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