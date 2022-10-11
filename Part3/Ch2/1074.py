n = int(input())

total = [[0]*(2**n)]*(2**n)

count = 0

def quater(arr):
    global count
    if len(arr) == 2:
        for i in range(2):
            for j in range(2):
                total[i][j] = count
                count +=1
    else:
        half = len(arr) // 2
        
                