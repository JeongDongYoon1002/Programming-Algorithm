N = int(input())
matrix = []
visit = [[0]*N for i in range(N)]

#상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    a = input()
    matrix.append(list(a))



def bfs(y,x):
    q = []
    q.append((y,x))
    
    while q:
        y,x = q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <N and 0<= nx <N :
                if visit[ny][nx] == 0 and matrix[y][x] == matrix[ny][nx]:
                    visit[ny][nx] = 1
        
                    q.append((ny,nx))

cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 :
            visit[i][j] = 1
            bfs(i,j)
            cnt += 1

print(cnt,end=' ')

for i in range(N):
    for j in range(N):
        if matrix[i][j] =='R':
            matrix[i][j] = 'G'

visit = [[0]*N for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 :
            visit[i][j] = 1
            bfs(i,j)
            cnt += 1
print(cnt)