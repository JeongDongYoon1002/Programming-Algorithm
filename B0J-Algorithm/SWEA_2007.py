t = int(input())
for i in range(t):
    s = input()
    for j in range(1,11):
        if s[:j] == s[j:2*j]:
            print('#{} {}'.format(i+1, j))

