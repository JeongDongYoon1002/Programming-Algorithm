def bfs(y,x):
    q = [(y,x)]
    cnt = 1
    visit[y][x] = 1
    while q:
        y,x = q.pop(0)
       

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx] == '1' and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny,nx))
                cnt += 1
    
    return cnt



n = int(input())
matrix = []
visit =[[0]*n for i in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0 , -1, 1]
for i in range(n):
    a = input()
    matrix.append(list(a))
result =[]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == '1' and visit[i][j] == 0:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for r in result:
    print(r)
