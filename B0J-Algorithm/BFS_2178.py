def bfs(q):
    

    while q:
        y, x = q.pop(0)
        if y == n-1 and x == m-1:
            print(visit[y][x])
            break 

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and matrix[ny][nx] == '1':
                visit[ny][nx] = visit[y][x] + 1
                q.append((ny,nx))
                



n, m = map(int,input().split()) # n 세로 m 가로
matrix = []
visit = [[0]*(m) for i in range(n)]
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    a = input()
    matrix.append(list(a))


q = [(0,0)]
visit[0][0] = 1
bfs(q)
