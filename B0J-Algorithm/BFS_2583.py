from collections import deque
def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    cnt = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0<= nx < m:
                if matrix[ny][nx] == 0 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    cnt += 1
                    q.append((ny,nx))
    return cnt      

def wall(fx, fy, lx, ly):
    for i in range(fy, ly):
        for j in range(fx, lx):
            matrix[i][j] = 1
        
n, m, k = map(int,input().split()) # n: 세로 m: 가로 k: 사각형의 갯수 
card = []
matrix = [[0]*m for i in range(n)]
visit = [[0]*m for i in range(n)]
# 상 하 좌 우 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(k):
    fx, fy, lx, ly = map(int,input().split())
    wall(fx, fy, lx, ly)

result = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and visit[i][j] == 0:
            result.append(bfs(i,j))

result.sort()
print(len(result))
for r in result:
    print(r, end=' ')