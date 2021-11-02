from collections import deque


n, m  = map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input())))

visit = [[0]*m for i in range(n)]
visit[0][0] = 1



def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q: 
        y, x = q.popleft()

        if y == n-1 and x == m-1 :
            print(visit[n-1][m-1])
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0 <= nx < m:
                if visit[ny][nx] < visit[y][x] and arr[ny][nx] == 1:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny,nx))

# 상 하 좌 우 
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

bfs(0,0)
print(visit)
