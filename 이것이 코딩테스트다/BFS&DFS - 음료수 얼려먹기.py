from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y,x))

    while q: 
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < n and 0<= nx <m:
                if visit[ny][nx] == 0 and arr[ny][nx] == 0:
                    
                    visit[ny][nx] = 1
                    q.append((ny,nx))


n, m = map(int,input().split()) # 세로 가로
arr = []
result = 0
#상 하 좌 우 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, input())))

visit = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and arr[i][j] == 0:
            visit[i][j] = 1
            bfs(i,j)
            result += 1

print(visit)
print(result)
