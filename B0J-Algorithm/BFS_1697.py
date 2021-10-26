n, k = map(int,input().split())
visit = [-1]*100001

visit[n] = 0
def dfs(x):
    q = [x]
    while q:
        x = q.pop(0)

        if 0 <= x-1 and visit[x-1] == -1:
            q.append(x-1)
            visit[x-1] = visit[x] + 1
        if x+1 <= 100000 and visit[x+1] == -1:
            q.append(x+1)
            visit[x+1] = visit[x] + 1
        if 2*x <= 100000 and visit[2*x] == -1:
            q.append(2*x)
            visit[2*x] = visit[x] + 1


dfs(n)
print(visit[k])