def solution(y, x):
    max_ = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            temp = 0
            for c in range(M):
                for r in range(M):
                    temp = temp + matrix[y+c][x+r]
                max_ = max(max_, temp)
    return max_



T = int(input())
for i in range(1, T+1):
    N, M = map(int,input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    result = solution(0,0)
    print('#{} {}'.format(i, result))


