def solution():
    global matrix
    result = ''
    for y in range(4):
        for x in range(4):
            if matrix[y][x] != 'T' or 'X' or 'O':
                continue

            if matrix[y][x] =='X' or 'O':
                # 우측
                if x + 3 == 3 and solve(matrix[y][x], y, x, 0, 1):
                    result = matrix[y][x] + ' won'
                    return result

                # 아래
                if y + 3 == 3 and solve(matrix[y][x], y, x, 1, 0):
                    result = matrix[y][x] + ' won'
                    return result

                # 우측 하단 대각선
                if y + 3 == 3 and x + 3 == 0 and solve(matrix[y][x], y, x, 1, 1):
                    result = matrix[y][x] + ' won'
                    return result

                # 좌측 하단 대각선
                if y == 0 and x == 3 and solve(matrix[y][x], y, x, 1, -1):
                    result = matrix[y][x] +' won'
                    return result

    return 'j'

def solve(shape, cy, cx, dy, dx):
    global matrix
    for z in range(1, 4):
        if matrix[cy+z*dy][cx+z*dx] != 'T' or matrix[cy+z*dy][cx+z*dx] != shape:
            return False
    return True


test_case = int(input())
for t in range(1, test_case+1):
    matrix = []
    for _ in range(4):
        matrix.append(list(input()))
    print("#{} {}".format(t, solution()))