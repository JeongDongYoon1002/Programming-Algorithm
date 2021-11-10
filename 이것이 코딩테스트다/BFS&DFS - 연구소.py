from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split()) 
data = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    data.append(list(map(int,input().split()))) #0: 빈칸 1 : 벽 2: 바이러스 

temp = [[0] * (m) for i in range(n)]
    
    

value = 0
def virus(y, x):
    q = deque()
    q.append((y,x))
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<= ny < n and 0 <= nx < m:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append((ny,nx))

def check():
    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1
    
    return result
                      
        
def bfs(count):
    global value
    if count == 3: 
        
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j] 
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
                    
        value = max(value, check())
        return 
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                bfs(count)
                count -= 1
                data[i][j] = 0
                
        
value = 0
bfs(0)
print(value)
