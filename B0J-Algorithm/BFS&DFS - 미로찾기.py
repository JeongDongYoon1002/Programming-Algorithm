import sys 
from collections import deque
input = sys.stdin.readline 

def bfs(y,x):
    q = deque()
    q.append((y,x))
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i] 
            
            if 0<= ny < n and 0<= nx <m:
                if data[ny][nx] == '1' and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny,nx))
                    
n, m = map(int,input().split()) # 세로 가로 

data = []
for i in range(n):
    data.append(list(input()))

visit = [[0]*m for i in range(n)]
visit[0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

bfs(0,0)


print(visit[n-1][m-1])
