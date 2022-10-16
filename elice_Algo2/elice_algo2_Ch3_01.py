isize = 0

def dfs(x, y, pMap, visited):
    global isize
    
    visited[x][y] = 1
    
    di = [(1,0), (0,1), (-1,0), (0,-1)]
    
    n = len(pMap)
    
    for d in di:
        nx = x+d[0]
        ny = y+d[1]
        
        if nx < 0 or ny < 0 or nx > n-1 or ny> n-1: continue
        if pMap[nx][ny] == 0: continue
        
        if not visited[nx][ny]:
            isize += 1
            dfs(nx, ny, pMap, visited)
        
def cadastralSurvey(pMap):
    
    global isize
    
    num_island = 0
    n = len(pMap)
    
    visited = []
    for i in range(n):
        visited.append([0 for j in range(n)])
    
    island_size = []
    for i in range(n):
        for j in range(n):
            if pMap[i][j] == 1 and visited[i][j] == 0:
                num_island += 1
                isize = 1
                dfs(i, j, pMap, visited)
                island_size.append(isize)

    island_size.sort()

    return (len(island_size), island_size)