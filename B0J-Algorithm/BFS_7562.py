# l = 체스판 한변의 길이 
# 나이트가 현재 있는 칸
# 나이트가 가야하는 칸 
from collections import deque

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 0
    while q:
        y, x = q.popleft()


        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < m and 0 <= nx <m :
                if visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                   
                    q.append((ny,nx))
                    matrix[ny][nx] = matrix[y][x] + 1
    


dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
result = []

m = int(input())
matrix = [[0]*m for i in range(m)]
visit = [[0]*m for i in range(m)]
a, b = map(int, input().split())
matrix[a][b] = 1
c, d = map(int,input().split())

bfs(a,b)
print(matrix[c][d]-1)
    