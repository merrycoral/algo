from collections import deque

def SNS(n_nodes, myInput, a, b):

    if a == b: return 0
    
    graph = [[] for i in range(n_nodes)]
    m_edges = len(myInput)
    
    #입력 정보로 그래프를 표현한다.
    for line in myInput:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
        
    #내가 누구와 연결되었는지 찾는것이므로 BFS가 적절
    
    queue = deque([a])
    visit = [0] * n_nodes
    
    visit[a] = 1
    #나(a)는 이미 방문한 것으로 처리
    
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if visit[node] == 0:
                visit[node] = visit[cur]+1
                queue.append(node)

    return visit[b]-1 if visit[b]>0 else -1
    # a를 방문처리 했기때문에 b는 +1 더 방문한 셈이므로 -1