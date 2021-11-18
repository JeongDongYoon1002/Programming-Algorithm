import sys
from collections import deque
input = sys.stdin.readline 

def bfs(y,x):
    q = deque()
    q.append((y,x))
    count = 1
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i] 
            
            if 0<= ny < n and 0<= nx < n:
                if visit[ny][nx] == 0 and data[ny][nx] == '1':
                    visit[ny][nx] = 1
                    q.append((ny,nx))
                    count += 1
        
    return count 

n = int(input())
data = []
for i in range(n):
    data.append(list(input()))
    
visit = [[0]*n for i in range(n)]
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = []
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and data[i][j] == '1':
            visit[i][j] = 1
            result.append(bfs(i,j))
            
print(len(result))
result.sort()
for r in result:
    print(r)            
            
