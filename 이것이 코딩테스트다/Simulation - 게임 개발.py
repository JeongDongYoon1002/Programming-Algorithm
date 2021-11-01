n, m = map(int,input().split()) #n 세로 m 가로 
y, x , direction = map(int,input().split()) # y 좌표, x 좌표 , 방향(0 북, 1 동, 2 남, 3 서)

matrix = [] 
for i in range(n):
    matrix.append(list(map(int, input().split())))


visit = [[0]*(m) for i in range(n)]
visit[y][x] = 1


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 1
turn_time = 0 

def turn_left():
    global direction
    direction = direction - 1
    if direction == -1:
        direction = 3

while True:
    turn_left()
    ny = y + dy[direction]
    nx = x + dx[direction]
    
    if visit[ny][nx] == 0 and matrix[ny][nx] == 0:
        visit[ny][nx] = 1
        y = ny 
        x = nx 
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1


    if turn_time == 4:
        ny = y - dy[direction]
        nx = x - dx[direction]

        if matrix[ny][nx] == 0:
            y = ny
            x = nx
        else:
            break 
        
        turn_time = 0

print(count)
