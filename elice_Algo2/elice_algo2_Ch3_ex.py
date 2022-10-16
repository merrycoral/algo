from collections import deque

friends = []

def bfs(x) :
    queue = deque([x])
    visit = [0]*n
    
    while queue:
        cur = queue.popleft()
        for i in range(n) :
            if friends[cur][i] == 1 and visit[i] == 0 :
                visit[i] = visit[cur] + 1
                queue.append(i)