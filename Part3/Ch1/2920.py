f = open("", 'r')
lines = f.readlines()

a = list(map(int, lines[0].split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if a[i] > a[i - 1]:
        descending = False
    elif a[i] < a[i - 1]:
        ascending = False

if ascending :
    print('ascending')
elif descending : 
    print('descending')
else:
    print('mixed')
    
    
