num = int(input('정사각형 크기는?'))

list = []
if num < 1:
  print('끝')
else :
  for i in range(num):
    a =''
    for j in range(num):
      a= a+str(((1+j+i)%10))
    list.append(a)
      

  for line in list:
    print(line)