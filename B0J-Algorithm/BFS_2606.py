def bfs(v):
    q = [v]
    visit[v] = 1
    cnt = 0
    while q:
        v = q.pop(0)
        for i in range(1, n+1):
            if visit[i] == 0 and matrix[v][i] == 1:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

n = int(input())
m = int(input())
matrix = [[0]*(n+1) for i in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a, b= map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1


print(bfs(1))