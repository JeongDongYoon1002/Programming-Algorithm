from itertools import combinations

n = int(input())
board = []
teacher = []
space = []

def watch(y, x, direction):
    if direction == 0 : # 위쪽 방향
        while y >= 0:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False

            y -= 1
    if direction == 1: #오른쪽 방향
        while x < n:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            x += 1

    if direction == 2: #아래쪽 방향
        while y < n:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False
            y += 1
    if direction == 3: # 왼쪽
        while x >= 0:
            if board[y][x] == 'S':
                return True
            if board[y][x] == 'O':
                return False

            x -= 1

    return False

def process():
    for y, x in teacher:
        for i in range(4):
            if watch(y,x,i):
                return True
    return False


for i in range(n):
    board.append(input().split())

    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i,j))
        if board[i][j] == 'X':
            space.append((i,j))
    
find =False

for data in combinations(space,3):
    for y, x in data:
        board[y][x] = 'O'
    if not process():
        find = True
        break
    
    for y, x in data:
        board[y][x] = 'X'

if find :
    print('YES')
else:
    print('NO')
