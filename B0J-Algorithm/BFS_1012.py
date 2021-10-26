def bfs(y,x):
    q = [(y,x)]
    while q:
        y, x = q.pop(0)
        visit[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0<= ny < n:
                if matrix[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((ny,nx))


test_case = int(input())
# 상 하 좌 우 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for a in range(test_case):
    m, n, k = map(int, input().split()) # m:가로 n: 세로 k: 배추의 갯수
    cnt = 0
    matrix = [[0]*m for i in range(n)]    
    visit = [[0]*m for i in range(n)]    
    for i in range(0, k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visit[i][j] == 0:
                bfs(i,j)
                cnt+=1
    print(cnt)
    
        

  