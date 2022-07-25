#우선순위 큐
import heapq

queue = []

#큐에 값을 넣을 때
heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print(queue)
#값을 뺄 때는 heappop을 사용
for index in range(len(queue)):
    print(heapq.heappop(queue))