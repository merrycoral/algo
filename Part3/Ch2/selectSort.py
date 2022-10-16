n = int(input())
arr = list()

for i in range(n):
    min_index = i
    for j in range(i+1, n): # i 다음부터 끝까지
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

for i in arr:
    print(i)    