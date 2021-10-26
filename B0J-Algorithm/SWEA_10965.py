
t = int(input())
for i in range(1, t+1):
    n = int(input())
    for j in range(1, n+1):
        temp = n*j
        num = temp **(1/2)
        if int(num) == num :
            print("#{} {}".format(i, j))
            break

        