n,m = map(int,input().split())
graph = []
w_location = []
b_location = []
for i in range(m):
    graph.append(list(map(str,input())))
    for j in range(n):
        if graph[i][j]=='W':
            w_location.append([i,j])
        else:
            b_location.append([i,j])
            
dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
def dfs(x,y,color):
    global cnt
    cnt+=1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<m and 0<=yy<n and graph[xx][yy]==color and visited[xx][yy]==0:
            visited[xx][yy] = visited[x][y]+1
            dfs(xx,yy,color)
           
# W 체크
visited = [[0]*n for _ in range(m)]
cnt_w = 0
for x,y in w_location:
    cnt = 0
    if visited[x][y]==0:
        visited[x][y] = 1
        dfs(x,y,'W')
    cnt_w += cnt*cnt
print(cnt_w,end=' ')
 
# B 체크
visited = [[0]*n for _ in range(m)]
cnt_b = 0
for x,y in b_location:
    cnt = 0
    if visited[x][y]==0:
        visited[x][y] = 1
        dfs(x,y,'B')
    cnt_b += cnt*cnt
print(cnt_b,end=' ')
