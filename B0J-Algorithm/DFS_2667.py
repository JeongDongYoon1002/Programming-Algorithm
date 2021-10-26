n = int(input())
matrix = []
visit = [[0]*n for i in range(n)]
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    a = input()
    matrix.append(list(a))


cnt = 0
def dfs(y,x):
    
    global cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < n and 0<= nx < n:
            if matrix[ny][nx] == '1' and visit[ny][nx] == 0 :
                visit[ny][nx] = 1
                cnt += 1
                dfs(ny,nx)

    

result = []
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and matrix[i][j] == '1':
            visit[i][j] = 1
            cnt = 1
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)    
