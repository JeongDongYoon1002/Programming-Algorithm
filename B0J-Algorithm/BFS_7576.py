from collections import deque

def bfs(q,a):
    
    while q:
        y,x, count = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if 0 <= ny < M and 0 <= nx < N:
                if matrix[ny][nx] == '0':
                    matrix[ny][nx] = '1'
                    q.append((ny,nx, count+1))
    
    return count 

N, M = map(int, input().split())
matrix = []
cnt = 0
for i in range(M):
    matrix.append(list(input().split()))


# 상 하 좌 우
dy = [-1, 1, 0 , 0]
dx = [0, 0, -1, 1]
q = deque()
answer = 0        

for i in range(M):
    for j in range(N):
        if matrix [i][j] == '1':
            q.append([i,j,answer])

result = bfs(q,answer)  

def check(answer, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '0':
                return -1
    return answer
print(check(result, matrix))
