from itertools import combinations
from copy import deepcopy
from collections import deque
Max=float('inf')
def NOE():
    for i in range(n):
        for j in range(m):
            if Map[i][j]==1:
                q.append((i,j))

def Attack(q):
    global k
    target = [(0,Max),(0,Max),(0,Max)]
    Dist = [Max,Max,Max]
    while q: #공격할 좌표 설정
        x,y = q.popleft()
        for i in range(3):
            z = abs(n-x) + abs(S[i]-y)
            if Dist[i] > z: # 좌표 갱신
                Dist[i] = z
                target[i] = (x,y)
            elif Dist[i] == z and y < target[i][1]: # 같은 거리일 때, 더 왼쪽에 있으면 좌표갱신
                target[i] = (x,y)
    for t,(x,y) in enumerate(target): #공격
        if Map[x][y] == 1:
            if Dist[t] <= d:
                Map[x][y] = 0
                k += 1



n,m,d = map(int,input().split())
D=[[*map(int,input().split())] for _ in range(n)]
Castle = [i for i in range(m)]
Archer = combinations(Castle,3)
ans = 0
q = deque()
for S in Archer:
    Map = deepcopy(D)
    k = 0
    while 1:
        NOE()
        if len(q) == 0: break
        Attack(q)
        Map = [[0]*m] + Map[:n-1] #아래로 한 칸 이동
    ans = max(ans,k)
print(ans)


