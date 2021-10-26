from collections import deque

def bfs(c):
    visit = [False] * (n+1)
    
    q = deque([start_node])
    visit[start_node] = True
    while q:
        x = q.popleft()
        
        for y, weight in matrix[x]:
            if not visit[y] and weight >= c:
                visit[y] = True
                q.append(y)
    
    return visit[end_node]
                

n, m = map(int,input().split())
matrix = [[] for i in range(n+1)]

start = 1
end = 1000000000
for _ in range(m):
    x, y, weight = map(int,input().split())
    matrix[x].append((y, weight))
    matrix[y].append((x, weight))
    start = min(start ,weight)
    end = max(end, weight)

start_node , end_node = map(int,input().split())
result = start

while start <= end:
    mid = (start+end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

