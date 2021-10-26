T = int(input())
for i in range(1, T+1):
    n = int(input())
    print('#{}'.format(i))
    matrix = [[0]*n for _ in range(n)]

    for _ in range(n):
        matrix[_][_] = 1
    
    for y in range(n):
        for x in range(y):
            if 0<= y-1:
                matrix[y][x] += matrix[y-1][x]
                if 0 <= x-1:
                    matrix[y][x] += matrix[y-1][x-1]
    
        print(*matrix[y][:y+1])