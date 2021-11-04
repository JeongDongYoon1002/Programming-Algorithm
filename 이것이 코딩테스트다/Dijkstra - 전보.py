import sys
import heapq 
input = sys.stdin.readline 
INF = int(1e9)

n, m, start = map(int,input().split()) # 도시 개수, 통로의 개수, 시작점 

graph = [[] for i in range(n+1)] # 그래프 배열 
distance = [INF] * (n+1) # 거리 무한대로 초기화

for i in range(m):
    a, b, c = map(int,input().split()) # a -> b : cost = c 
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용, 노드 
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) 

        if distance[now] < dist : # 한번 접근한 노드라면 ? -> 재시작
            continue

        for i in graph[now]:
            cost = dist + i[1] # 다음 접근하 노드의 비용 

            if cost < distance[i[0]] :
                distance[i[0]] = cost 

                heapq.heappush(q, (cost, i[0]))

count = 0
time = 0
for i in graph[start]:
    count += 1
    time = max(time, i[1])

print(count, end =" ")
print(time)






    
