INF = int(1e9)
n, m = map(int,input().split()) # n : 회새 갓수 m : 간선
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1



x, k = map(int,input().split())



for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


print(graph[1][k] + graph[k][x])

