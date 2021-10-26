def check():
    global N, M
    for i in range(N):
        if M % 2 == 0 :
            return False
        M //= 2
    return True
T = int(input())
for i in range(1, T+1):
    N, M = map(int,input().split())
    if check() :
        print("#{} {}".format(i,'ON'))
    else:
        print("#{} {}".format(i,'OFF'))
