
from collections import deque
def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    while q:
        y, x= q.popleft()
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < m and 0<= nx < n:
                if matrix[y][x] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((ny,nx))


n , m = map(int,input().split()) #n: 가로 m : 세로
matrix = []
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
visit = [[0]*(n) for i in range(m)]
cnt = 0
for i in range(m):
    a = map(int,input().split())
    matrix.append(list(a))

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1 and visit[i][j] == 0:
            bfs(i,j)
            cnt += 1
print(cnt)
