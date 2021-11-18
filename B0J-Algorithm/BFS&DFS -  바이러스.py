import sys
from collections import deque 
input = sys.stdin.readline 


def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    count = 0
    while q:
        v = q.popleft()
        
        for i in range(1, n+1):
            if graph[v][i] == 1 and visit[i] == 0:
                visit[i] = 1
                q.append(i)
                count += 1
    return count
                
            
n = int(input())
m = int(input())

graph = [[0]*(n+1) for i in range(n+1)]
visit = [0]*(n+1)


for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    

print(bfs(1))
