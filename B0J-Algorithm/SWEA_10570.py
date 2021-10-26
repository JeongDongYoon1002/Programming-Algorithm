
import math
def check():
    global A, B
    cnt = 0
    for i in range(A, B+1):
        c = i **(1/2)
        if c == int(c):
            i = str(i)
            c = str(int(c))
            if i == i[::-1] and c == c[::-1]:
                cnt += 1 
    return cnt
            

        

T = int(input())
for i in range(1, T+1):
    A, B = map(int,input().split())
    print("#{} {}".format(i, check()))
