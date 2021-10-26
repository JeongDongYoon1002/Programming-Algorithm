def bfs(v):
    q = [v]
    global result_bfs
    while q:
        v = q.pop(0)
        visit[v] = 1
        result_bfs.append(v)
        for i in range(1, n+1):
            if visit[i] == 0 and matrix[v][i] ==1:
                visit[i] = 1
                q.append(i)

        
def dfs(v):
    global result_dfs
    visit[v] = 1
    result_dfs.append(v)
    for i in range(1, n+1):
        if visit[i] == 0 and matrix[v][i] ==1:
            dfs(i)

n, m, v = map(int,input().split())
matrix = [[0]*int(n+1) for i in range(n+1)]
visit = [0] *(n+1)
for i in range(m):
    a , b = map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
result_dfs = []
result_bfs = []
dfs(v)
for r in result_dfs:
    print(r, end =' ')
visit = [0] *(n+1)
bfs(v)
print()
for r in result_bfs:
    print(r, end=' ')
