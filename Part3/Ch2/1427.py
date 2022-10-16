n = list(input())

for i in range(len(n)):
    max_in = i
    for j in range(i+1, len(n)):
        if n[max_in] < n[j]:
            max_in = j
    n[i], n[max_in] = n[max_in], n[i]