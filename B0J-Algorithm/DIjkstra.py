import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n, m , start = map(int,input().split()) # n: 도시의갯수, m : 통로의갯수, start = 시작
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost

                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
value = 0
num = 0
for i in range(len(distance)):
    if distance[i] != INF:
        num += 1
        value = max(value, distance[i])
print(distance)
print(num-1, end=' ')
print(value)
